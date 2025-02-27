from itertools import permutations

def palindromes_between_indices(s):
    substr = s[:3].lower()
    english_letters = ''.join(filter(str.isalpha, substr))
    palindromes = set()
    for length in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes