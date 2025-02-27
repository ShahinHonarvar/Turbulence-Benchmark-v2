def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[4:9])).lower()
    return {word for word in set(permutations(letters)) if word == word[::-1]}