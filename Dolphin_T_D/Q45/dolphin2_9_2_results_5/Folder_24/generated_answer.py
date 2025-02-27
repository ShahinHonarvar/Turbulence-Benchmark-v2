from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:10]
    subset = set()
    for p in range(4, len(substring)):
        for perm in permutations(substring, p):
            word = ''.join(perm)
            word_lower = word.lower()
            if word_lower == word_lower[::-1]:
                subset.add(word)
    return subset