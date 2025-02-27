def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[2:7])).lower()
    return {word for word in {''.join(p) for p in permutations(letters)} if len(word) >= 3 and word == word[::-1]}