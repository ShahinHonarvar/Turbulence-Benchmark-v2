from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    english_letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    if len(english_letters) < 5:
        return palindromes
    for length in range(5, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes