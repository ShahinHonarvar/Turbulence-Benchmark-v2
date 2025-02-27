from itertools import permutations

def palindromes_between_indices(s):
    valid_chars = [c.lower() for c in s[3:8] if c.isalpha()]
    palindromes = set()
    for p in permutations(valid_chars):
        if len(valid_chars) >= 5 and p == p[::-1]:
            palindromes.add(''.join(p))
    return {palindrome for palindrome in palindromes if len(palindrome) >= 5}