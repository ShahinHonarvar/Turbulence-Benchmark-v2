from itertools import permutations

def palindromes_between_indices(s):
    start, end = (2, 8)
    sub_str = ''.join(filter(str.isalpha, s[start:end + 1])).lower()
    palindromes = set()
    for length in range(4, len(sub_str) + 1):
        for perm in set(permutations(sub_str, length)):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes