from itertools import permutations

def palindromes_between_indices(s):
    sub_s = s[5:8].lower()
    palindromes = set()
    for p in permutations(sub_s):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes