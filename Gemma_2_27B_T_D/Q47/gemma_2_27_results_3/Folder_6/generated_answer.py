def palindromes_of_specific_lengths(text):
    return set([word.lower() for word in text[45:99].split() if len(word) in range(40, 48) and word.lower() == word.lower()[::-1]])