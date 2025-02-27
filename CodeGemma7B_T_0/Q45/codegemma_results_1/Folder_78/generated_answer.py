def palindromes_between_indices(text):
    text = text.lower()
    text = text[6:9]
    if not text.isalpha():
        return set()
    if len(text) < 3:
        return set()
    return {text[i:j + 1] for i in range(len(text)) for j in range(i, len(text)) if text[i:j + 1] == text[i:j + 1][::-1]}