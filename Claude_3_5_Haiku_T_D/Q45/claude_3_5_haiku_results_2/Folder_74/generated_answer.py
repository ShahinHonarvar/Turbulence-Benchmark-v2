from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    palindrome_set = set()
    for perm_length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, perm_length)):
            for palindrome in generate_palindromes(perm):
                if len(palindrome) >= 6:
                    palindrome_set.add(palindrome)
    return palindrome_set

def generate_palindromes(chars):
    palindromes = set()
    for p in set(permutations(chars)):
        p_str = ''.join(p)
        if p_str == p_str[::-1]:
            palindromes.add(p_str)
    return palindromes