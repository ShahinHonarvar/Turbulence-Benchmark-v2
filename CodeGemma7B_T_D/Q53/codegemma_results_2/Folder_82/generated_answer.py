def palindrome_of_length_at_least_n(text):
    text = text.lower()
    pals = set()
    for i in range(len(text)):
        for j in range(i + 72, len(text) + 1):
            if text[i:j] == text[j - 1:i - 1:-1]:
                pals.add(text[i:j])
    return pals