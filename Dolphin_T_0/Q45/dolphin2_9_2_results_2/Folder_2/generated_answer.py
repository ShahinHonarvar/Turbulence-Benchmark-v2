def palindromes_between_indices(s):
    letters = ''.join(sorted([char.lower() for char in s]))
    return {word for word in set(letters) if len(word) >= 6 and word == word[::-1]}