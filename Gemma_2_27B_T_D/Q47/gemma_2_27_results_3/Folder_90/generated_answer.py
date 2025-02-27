def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[106:281].split()) if word.lower() == word.lower()[::-1] and 136 <= len(word) <= 151 and word.isalpha()}