from itertools import permutations

def palindromes_between_indices(s):
    indices_range = s[3:6].lower()
    english_letters = ''.join(filter(str.isalpha, indices_range))
    if len(english_letters) < 3:
        return set()
    unique_perms = set(permutations(english_letters))
    palindromes = set()
    for perm in unique_perms:
        if len(perm) >= 3:
            for length in range(3, len(perm) + 1):
                for i in range(len(perm) - length + 1):
                    substring = perm[i:i + length]
                    if substring == substring[::-1]:
                        palindromes.add(''.join(substring))
    return palindromes