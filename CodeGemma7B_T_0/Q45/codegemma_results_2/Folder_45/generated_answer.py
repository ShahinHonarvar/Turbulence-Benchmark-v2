def palindromes_between_indices(text):
    text = text.lower()
    if not text[5:10].isalpha():
        return set()
    return {text[i:i + 4] for i in range(5, len(text) - 3) if text[i:i + 4] == text[i:i + 4][::-1]}