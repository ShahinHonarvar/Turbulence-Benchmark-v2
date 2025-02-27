def palindromes_of_specific_lengths(text):
    return set((x for x in [word for word in text[2:9] if word.isalpha() and len(word) in [3, 4] and (word.lower() == word[::-1].lower())]))