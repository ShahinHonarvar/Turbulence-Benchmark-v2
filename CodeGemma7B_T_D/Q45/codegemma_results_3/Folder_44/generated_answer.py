from itertools import permutations

def palindromes_between_indices(string):
    length = 5
    valid = set()

    def is_valid(word):
        for letter in word:
            if letter not in string[2:8]:
                return False
        return True
    for letters in permutations(string[2:8], length):
        word = ''.join(letters)
        if is_valid(word):
            valid.add(word)
    return valid