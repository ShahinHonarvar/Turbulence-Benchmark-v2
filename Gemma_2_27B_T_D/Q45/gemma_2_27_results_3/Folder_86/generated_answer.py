def palindromes_between_indices(text):
    substring = text[6:10]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    return {word for word in {''.join(p) for p in permutations(letters)} if len(word) >= 4 and word == word[::-1]}