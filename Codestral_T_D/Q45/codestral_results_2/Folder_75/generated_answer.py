from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[2:5].lower()
    palindromes = set()
    for i in range(3, len(sub_str) + 1):
        for p in permutations(sub_str, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes