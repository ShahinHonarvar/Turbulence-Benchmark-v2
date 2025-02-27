from itertools import permutations

def palindromes_between_indices(word):
    result = set()
    for p in permutations(word[2:6]):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            result.add(palindrome.lower())
    return result or {}