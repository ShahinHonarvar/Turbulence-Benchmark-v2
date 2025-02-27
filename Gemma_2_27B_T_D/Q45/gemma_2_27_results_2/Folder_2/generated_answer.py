from itertools import permutations

def palindromes_between_indices(text):
    letters = text[1:6].lower()
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1] and len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes