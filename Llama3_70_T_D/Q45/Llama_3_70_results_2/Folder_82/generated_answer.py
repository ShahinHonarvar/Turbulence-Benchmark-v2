import itertools

def palindromes_between_indices(s):
    s = s.lower()
    substr = s[1:7]
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for p in itertools.permutations(letters):
        word = ''.join(p)
        if len(word) >= 7 and word == word[::-1]:
            palindromes.add(word)
    return palindromes