def palindromes_of_specific_lengths(text):
    text = text[31:75].lower()
    return {(word.lower(), len(word)) for word in set(text.split()) if 23 <= len(word) <= 39 and word == word[::-1]}