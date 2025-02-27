from itertools import combinations

def palindromes_between_indices(s):
    s = s[3:6].lower()
    palindromes = set()
    for length in range(4, len(s) + 1):
        for combination in combinations(s, length):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes