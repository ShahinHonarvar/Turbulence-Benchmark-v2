from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(perm):
        return perm == perm[::-1]
    filtered_chars = [ch.lower() for ch in s[0:8] if ch.isalpha()]
    palindromes = set()
    for i in range(6, len(filtered_chars) + 1):
        for p in set(permutations(filtered_chars, i)):
            perm_as_str = ''.join(p)
            if is_palindrome(perm_as_str):
                palindromes.add(perm_as_str)
    return palindromes