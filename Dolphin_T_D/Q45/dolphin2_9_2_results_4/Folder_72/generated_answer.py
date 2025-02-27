from itertools import permutations

def palindromes_between_indices(s):
    index_start = 0
    index_end = 6
    substring = s[index_start:index_end + 1]
    palindromes = set()
    for i in range(6, len(substring)):
        for j in permutations(substring, i):
            word = ''.join(j)
            if word == word[::-1] and word.islower() not in palindromes:
                palindromes.add(word.islower())
    return palindromes