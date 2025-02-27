from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_str = s[4:8]
    english_letters = ''.join(filter(str.isalpha, sub_str))
    potential_palindromes = set()
    for perm in permutations(english_letters):
        candidate = ''.join(perm)
        if len(candidate) >= 5 and candidate == candidate[::-1]:
            potential_palindromes.add(candidate)
    return potential_palindromes