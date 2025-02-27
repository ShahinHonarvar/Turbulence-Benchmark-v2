def palindromes_of_specific_lengths(text):
    return {word for word in set(text[101:293].lower().split()) if word == word[::-1] and 154 <= len(word) <= 182 and word.isalpha()}