import itertools

def palindromes_between_indices(text):
    result = set()
    for word in itertools.permutations(text[0:5].lower(), 5):
        word = ''.join(word)
        if word == word[::-1] and len(word) >= 4 and word.isalpha():
            result.add(word)
    return result