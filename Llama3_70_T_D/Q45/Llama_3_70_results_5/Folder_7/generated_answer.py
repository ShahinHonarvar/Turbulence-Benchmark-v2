from itertools import permutations, combinations_with_replacement

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[1:10] if c.isalpha()]
    letters_set = set(letters)
    result = set()
    for r in range(7, len(letters) + 1):
        for combo in combinations_with_replacement(letters_set, r):
            for perm in permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    result.add(word)
    return result