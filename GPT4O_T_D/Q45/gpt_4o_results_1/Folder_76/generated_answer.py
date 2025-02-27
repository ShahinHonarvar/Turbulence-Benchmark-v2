from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substring = s[1:5].lower()
    english_letters = [char for char in substring if 'a' <= char <= 'z']
    palindromes = set()
    for perm in set(permutations(english_letters)):
        perm_string = ''.join(perm)
        for length in range(4, len(perm_string) + 1):
            for i in range(len(perm_string) - length + 1):
                candidate = perm_string[i:i + length]
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes