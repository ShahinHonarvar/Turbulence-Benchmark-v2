from itertools import permutations

def palindromes_between_indices(s):
    sub_s = s[6:9]
    palindromes = set()
    for p in permutations(sub_s, len(sub_s)):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes