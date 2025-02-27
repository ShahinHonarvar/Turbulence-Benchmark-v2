from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    english_letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for perm in permutations(english_letters):
        for length in range(6, len(perm) + 1):
            candidates = perm[:length]
            if candidates == candidates[::-1]:
                palindromes.add(''.join(candidates))
    return palindromes