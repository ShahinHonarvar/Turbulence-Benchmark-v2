def palindromes_of_specific_lengths(text):
    return {word for word in set(''.join(filter(str.isalpha, text[32:80].lower())).split()) if word == word[::-1] and 35 <= len(word) <= 41}