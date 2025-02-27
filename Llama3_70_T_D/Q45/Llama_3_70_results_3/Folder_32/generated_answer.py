from itertools import permutations, combinations_with_replacement

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in combinations_with_replacement(letters, r):
            for perm in permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes