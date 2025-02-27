def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[1:300].split()) if 3 <= len(word) <= 10 and word.lower() == word.lower()[::-1] and word.isalpha()}