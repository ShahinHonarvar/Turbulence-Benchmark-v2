from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10]
    letters = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            perm_str = ''.join(perm)
            for i in range(len(perm_str) - length + 1):
                candidate = perm_str[i:i + length]
                if candidate == candidate[::-1] and len(candidate) >= 3:
                    palindromes.add(candidate)
    return palindromes