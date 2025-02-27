import itertools

def palindromes_between_indices(s):
    letters = ''.join(sorted(set(s[4:9])))
    palindromes_set = set()
    for l in range(3, len(letters) + 1):
        for p in itertools.permutations(letters, l):
            word = ''.join(p)
            if word == word.lower() and word == word[::-1]:
                palindromes_set.add(word)
    return palindromes_set