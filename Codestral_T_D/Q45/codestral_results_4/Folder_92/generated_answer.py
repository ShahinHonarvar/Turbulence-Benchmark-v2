import itertools

def palindromes_between_indices(s):
    s = s[4:8].lower()
    palindromes = set()
    for p in itertools.permutations(s, len(s)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes