def palindromes_of_specific_lengths(text):
    return {word for word in set(text[30:96].split()) if word.lower() == word.lower()[::-1] and len(word) in range(34, 56)}