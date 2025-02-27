def palindromes_between_indices(text):
    letters = text[3:10]
    return {word for word in {''.join(p) for p in permutations(letters)} if len(word) >= 3 and word.lower() == word[::-1].lower()}