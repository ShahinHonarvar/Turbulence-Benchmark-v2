def palindromes_between_indices(text):
    text = text.lower()
    if not text[5:7].isalpha():
        return set()
    return {text[i:i + 3] for i in range(5, 7) for j in range(i, 7) for k in range(j, 7) if text[i] == text[j] and text[j] == text[k]}