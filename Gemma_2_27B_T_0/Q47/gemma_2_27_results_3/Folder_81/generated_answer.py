def palindromes_of_specific_lengths(text):
    return {word for word in set(text[12:123].lower().split()) if word == word[::-1] and 12 <= len(word) <= 220 and word.isalpha()}