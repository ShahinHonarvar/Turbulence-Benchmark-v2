import itertools

def palindromes_between_indices(s):
    string = s[3:7]
    palindromes = set()
    for i in range(4, len(string) + 1):
        for words in itertools.permutations(string, i):
            word = ''.join(words).lower()
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes