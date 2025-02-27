from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:9].lower()
    palindromes = set()
    for r in range(5, len(sub_str) + 1):
        for p in permutations(sub_str, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes