from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    palindromes = set()
    substrings = [s[i:j] for i in range(4) for j in range(i + 3, len(s) + 1)]
    for substring in substrings:
        for p in permutations(substring.lower()):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes