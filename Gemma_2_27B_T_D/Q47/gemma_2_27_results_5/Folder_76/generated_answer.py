def palindromes_of_specific_lengths(text):
    return {word.lower() for word in set(text[101:293].split()) if len(word) in range(154, 183) and word.lower() == word[::-1].lower() and word.isalnum()}