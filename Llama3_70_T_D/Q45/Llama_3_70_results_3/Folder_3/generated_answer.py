import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[7:10] if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes