import itertools

def palindromes_between_indices(string):
    s = string[2:9].lower()
    letters = [letter for letter in s if letter.isalpha()]
    result = set()
    if len(letters) >= 7:
        for perm in itertools.permutations(letters):
            word = ''.join(perm)
            if word == word[::-1] and len(word) >= 7:
                result.add(word)
    return result