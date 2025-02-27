from itertools import permutations, combinations_with_replacement

def palindromes_between_indices(s):
    s = s[7:10].lower()
    letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in set(permutations(letters, length)):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes