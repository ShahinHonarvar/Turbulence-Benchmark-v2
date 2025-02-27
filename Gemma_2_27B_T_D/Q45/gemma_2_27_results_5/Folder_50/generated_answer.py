def palindromes_between_indices(text):
    letters = ''.join((letter for letter in text[4:9] if letter.isalpha())).lower()
    return {word for word in {''.join(combination) for combination in itertools.permutations(letters)} if word == word[::-1] and len(word) >= 5}