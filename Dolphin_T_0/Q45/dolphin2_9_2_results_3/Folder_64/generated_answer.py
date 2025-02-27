from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(string):
    indices = range(4, 10)
    letters = [char.lower() for char in string if char in ascii_letters]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes