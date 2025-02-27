from itertools import combinations, permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combination in combinations(letters, length):
            for perm in permutations(combination):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes