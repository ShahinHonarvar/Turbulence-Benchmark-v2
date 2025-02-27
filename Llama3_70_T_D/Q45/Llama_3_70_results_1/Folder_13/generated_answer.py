import itertools

def palindromes_between_indices(s):
    s = s[3:10].lower()
    result = set()
    for length in range(5, len(s) + 1):
        for combo in itertools.combinations(s, length):
            for perm in set(itertools.permutations(combo)):
                word = ''.join(perm)
                if word == word[::-1]:
                    result.add(word)
    return result