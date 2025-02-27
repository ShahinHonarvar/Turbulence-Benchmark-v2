def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[18:89].split()) if word.isalnum() and len(word) in range(12, 15) and (word.lower() == word.lower()[::-1])}