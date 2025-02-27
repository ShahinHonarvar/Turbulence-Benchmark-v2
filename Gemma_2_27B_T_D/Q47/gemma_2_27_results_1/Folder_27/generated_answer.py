def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[13:100].split()) if len(word) in range(26, 30) and word.lower() == word.lower()[::-1] and word.isalpha()}