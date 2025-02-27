from itertools import permutations

def palindromes_between_indices(s):
    relevant_chars = ''.join([c for c in s[6:10] if c.isalpha()]).lower()
    palindromes = set()
    for length in range(3, len(relevant_chars) + 1):
        for p in permutations(relevant_chars, length):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes