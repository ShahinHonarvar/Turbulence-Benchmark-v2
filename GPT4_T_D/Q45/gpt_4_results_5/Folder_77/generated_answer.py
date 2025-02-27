from itertools import permutations

def palindromes_between_indices(text):
    subset_str = text[4:7].lower()
    palindromes = set()
    for i in range(4, len(subset_str) + 1):
        perm = set([''.join(p) for p in permutations(subset_str, i)])
        for word in perm:
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes