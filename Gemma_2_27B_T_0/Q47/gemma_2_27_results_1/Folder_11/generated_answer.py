def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[24:98].split()) if len(word) in range(10, 37) and word.lower() == word.lower()[::-1] and word.isalpha()}