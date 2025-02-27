import itertools

def palindromes_between_indices(s):
    s = s[1:8].lower()
    palindromes = set()
    for length in range(3, len(s) + 1):
        for combo in itertools.permutations(s, length):
            word = ''.join(combo)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes