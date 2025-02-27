from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    characters = text[2:7]
    filtered_chars = [char for char in characters if char.isalpha()]
    for i in range(4, len(filtered_chars) + 1):
        for item in permutations(filtered_chars, i):
            word = ''.join(item)
            if word.lower() == word[::-1].lower():
                result.add(word.lower())
    return result