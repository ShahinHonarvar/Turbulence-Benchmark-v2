def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[100:201].split()) if word.lower() == word.lower()[::-1] and 5 <= len(word) <= 10 and word.isalpha()}