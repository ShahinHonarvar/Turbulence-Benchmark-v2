from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    characters = text[2:6]
    filtered_characters = ''.join((ch for ch in characters if ch.isalpha())).lower()
    for i in range(5, len(filtered_characters) + 1):
        for item in permutations(filtered_characters, i):
            word = ''.join(item)
            if word == word[::-1]:
                result.add(word)
    return result