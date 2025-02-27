from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[2:4].lower()
    palindromes = set()
    for i in range(3, len(sub_str) + 1):
        for perm in permutations(sub_str, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes