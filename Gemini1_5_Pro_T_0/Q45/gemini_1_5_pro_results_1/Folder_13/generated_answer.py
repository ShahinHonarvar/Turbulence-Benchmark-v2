from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[3:10].lower()
    letters = [letter for letter in s if letter.isalpha()]
    if len(letters) >= 5:
        for i in range(5, len(letters) + 1):
            for item in permutations(letters, i):
                word = ''.join(item)
                if word == word[::-1]:
                    result.add(word)
    return result