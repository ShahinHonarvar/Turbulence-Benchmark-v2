import itertools

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                word = ''.join(perm)
                if word == word[::-1] and word not in palindromes:
                    palindromes.add(word)
    return palindromes