from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:7].lower()
    english_letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for length in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes