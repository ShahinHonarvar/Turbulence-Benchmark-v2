def palindromes_of_specific_lengths(text):
    text = text.lower()
    return {word for word in text[123:284] if len(word) in range(115, 135) and word == word[::-1]}