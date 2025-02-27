def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[4:9]))
    return {word for word in set((''.join(p) for n in range(3, len(letters) + 1) for p in permutations(letters, n))) if word.lower() == word[::-1].lower()}