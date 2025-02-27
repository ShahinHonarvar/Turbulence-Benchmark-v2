import itertools

def palindromes_between_indices(s):
    substring = s[1:10].lower()
    palindromes = set()
    for length in range(7, len(substring) + 1):
        for perm in itertools.permutations(substring, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes