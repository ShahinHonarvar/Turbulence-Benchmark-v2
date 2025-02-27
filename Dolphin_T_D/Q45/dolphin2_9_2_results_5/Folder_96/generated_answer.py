from itertools import permutations

def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[3:9] if ch.isalpha()]
    if len(''.join(letters)) < 12:
        return set()
    else:
        result = set()
        for p in permutations(letters, len(''.join(letters)) // 2):
            word = ''.join(p) + ''.join(reversed(p))
            result.add(word)
        return result