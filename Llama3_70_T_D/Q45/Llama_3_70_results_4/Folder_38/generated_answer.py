from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes