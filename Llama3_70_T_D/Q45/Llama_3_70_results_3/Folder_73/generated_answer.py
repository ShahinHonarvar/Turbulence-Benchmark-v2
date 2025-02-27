import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:7] if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes