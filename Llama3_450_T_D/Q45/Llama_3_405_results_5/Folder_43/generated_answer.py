from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [char.lower() for char in s[2:6] if char.isalpha()]
    letters_set = set(english_letters)
    palindromes = set()
    for r in range(4, len(english_letters) + 1):
        for p in permutations(letters_set, r):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                palindromes.add(p_str)
    return palindromes