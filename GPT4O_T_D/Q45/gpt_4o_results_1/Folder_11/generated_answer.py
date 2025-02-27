from itertools import permutations

def palindromes_between_indices(s):
    subrange = s[3:8]
    english_letters = ''.join(filter(str.isalpha, subrange)).lower()
    palindromes = set()
    for length in range(4, len(english_letters) + 1):
        for perm in set(permutations(english_letters, length)):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes