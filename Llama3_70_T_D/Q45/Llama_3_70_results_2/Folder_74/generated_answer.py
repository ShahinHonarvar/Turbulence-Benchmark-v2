from itertools import permutations, combinations_with_replacement

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for combo in combinations_with_replacement(letters, length):
            for perm in permutations(combo, length):
                word = ''.join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes