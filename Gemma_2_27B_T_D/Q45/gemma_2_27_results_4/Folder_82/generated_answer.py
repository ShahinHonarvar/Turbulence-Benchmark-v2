from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[1:7])).lower()
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        if len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes