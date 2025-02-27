from itertools import permutations

def palindromes_between_indices(s):
    chars = [c for c in s[2:8]]
    palindromes = set()
    for p in permutations(chars, int((len(chars) + 1) / 2)):
        word = ''.join(p)
        if len(word) >= 6 and word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes