from itertools import permutations

def palindromes_between_indices(s):
    relevant_chars = ''.join(filter(str.isalpha, s[1:6])).lower()
    palindromes = set()
    for perm in permutations(relevant_chars):
        joined = ''.join(perm)
        if len(joined) >= 6 and joined == joined[::-1]:
            palindromes.add(joined)
    return palindromes