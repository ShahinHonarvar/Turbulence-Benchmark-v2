def palindromes_of_specific_lengths(text):
    text = ''.join([c for c in text.lower() if c.isalpha()])
    return {text[i:i + l] for l in range(49, 52) for i in range(27, 96) if text[i:i + l] == text[i:i + l][::-1]}