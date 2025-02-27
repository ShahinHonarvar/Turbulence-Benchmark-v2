def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[16:77]) if word.lower() == word.lower()[::-1] and 43 <= len(word) <= 47 and word.isalpha()}