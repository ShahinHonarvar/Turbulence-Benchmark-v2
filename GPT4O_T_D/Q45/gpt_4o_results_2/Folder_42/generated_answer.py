from itertools import permutations

def palindromes_between_indices(s):
    s_range = s[6:10].lower()
    s_filtered = ''.join(filter(str.isalpha, s_range))
    palindromes = set()
    for perm in set(permutations(s_filtered)):
        for length in range(3, len(perm) + 1):
            word = ''.join(perm[:length])
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes