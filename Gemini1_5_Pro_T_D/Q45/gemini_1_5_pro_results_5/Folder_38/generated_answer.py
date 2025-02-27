from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    string = string[3:9].lower()
    letters = [char for char in string if char.isalpha()]
    if len(letters) >= 5:
        for i in range(5, len(letters) + 1):
            for item in permutations(letters, i):
                word = ''.join(item)
                if word == word[::-1]:
                    result.add(word)
    return result