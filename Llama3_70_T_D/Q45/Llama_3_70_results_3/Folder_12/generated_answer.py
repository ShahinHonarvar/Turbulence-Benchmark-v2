import itertools

def palindromes_between_indices(s):
    s = s[3:9].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(4, len(s) + 1):
        for combo in itertools.combinations(s, r):
            for perm in itertools.permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes