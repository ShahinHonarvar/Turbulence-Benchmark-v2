from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5].lower()
    english_letters = ''.join(filter(str.isalpha, substring))
    potential_palindromes = set()
    for perm in set(permutations(english_letters, len(english_letters))):
        candidate = ''.join(perm)
        for i in range(0, len(candidate) - 4 + 1):
            segment = candidate[i:i + 5]
            if segment == segment[::-1]:
                potential_palindromes.add(segment)
    return potential_palindromes