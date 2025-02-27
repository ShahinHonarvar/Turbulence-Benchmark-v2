from itertools import permutations

def palindromes_between_indices(text):
    letters = text[3:7].lower()
    palindromes = set()
    for perm in permutations(letters):
        palindrome_candidate = ''.join(perm)
        if palindrome_candidate == palindrome_candidate[::-1] and len(palindrome_candidate) >= 4:
            palindromes.add(palindrome_candidate)
    return palindromes