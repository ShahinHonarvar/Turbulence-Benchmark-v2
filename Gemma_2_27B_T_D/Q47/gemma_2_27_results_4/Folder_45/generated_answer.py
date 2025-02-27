def palindromes_of_specific_lengths(text):
    return {word for word in set([word for word in text[70:141] if word.isalpha() and len(word) in range(3, 61) and (word.lower() == word[::-1].lower())])}