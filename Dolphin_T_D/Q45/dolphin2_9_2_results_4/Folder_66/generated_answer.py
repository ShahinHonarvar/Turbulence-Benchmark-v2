import itertools

def palindromes_between_indices(s):
    s = s.lower()
    substrings = set()
    substrings.add(s[0:6])
    substrings.add(s[1:7])
    substrings.add(s[2:8])
    substrings.add(s[3:9])
    substrings.add(s[4:10])
    palindromes = set()
    for subset in substrings:
        for word in itertools.permutations(subset, 5):
            word = ''.join(word)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes