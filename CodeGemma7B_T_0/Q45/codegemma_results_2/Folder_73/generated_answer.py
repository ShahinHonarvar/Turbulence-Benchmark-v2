def palindromes_between_indices(text):
    text = text.lower()
    if not text[3:7].isalpha():
        return set()
    return {text[i:j] for i in range(3, 7) for j in range(i + 1, 7 + 1) if text[i:j] == text[j - 1:i - 1:-1]}