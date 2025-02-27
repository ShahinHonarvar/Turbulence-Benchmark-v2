from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    english_letters = ''.join(filter(str.isalpha, s))
    unique_palindromes = set()
    for perm in permutations(english_letters):
        for length in range(3, len(english_letters) + 1):
            substr = perm[:length]
            if substr == substr[::-1]:
                unique_palindromes.add(substr)
    return unique_palindromes