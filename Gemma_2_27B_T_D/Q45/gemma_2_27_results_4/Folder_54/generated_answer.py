def palindromes_between_indices(text):
    letters = ''.join([char for char in text[4:10].lower() if char.isalpha()])
    return {word for word in {''.join(reversed(perm)) for perm in permutations(letters)} if len(word) >= 4 and word == word[::-1]}