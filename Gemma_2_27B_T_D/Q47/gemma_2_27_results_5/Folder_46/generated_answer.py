def palindromes_of_specific_lengths(text):
    return {word for word in set(text[11:98].lower().split()) if word == word[::-1] and 29 <= len(word) <= 62}