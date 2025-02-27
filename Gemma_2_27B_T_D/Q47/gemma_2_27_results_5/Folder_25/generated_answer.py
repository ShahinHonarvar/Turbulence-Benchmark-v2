def palindromes_of_specific_lengths(text):
    return {word for word in set([text[i:j + 1].lower() for i in range(26, 85 - j) for j in range(29, 47)]) if word == word[::-1] and word.isalpha()}