def palindromes_of_specific_lengths(text):
    return {word for word in set((i for i in text[31:75] if i.isalpha())) if word.lower() == word.lower()[::-1] and len(word) in range(23, 40)}