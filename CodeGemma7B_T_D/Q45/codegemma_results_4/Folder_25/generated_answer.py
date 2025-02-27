def palindromes_between_indices(text):
    word = text[1:5].lower()[::-1]
    for _ in range(4 - len(word)):
        word += word[-1]
    return set([word]) if word in text[4:].lower() else set()