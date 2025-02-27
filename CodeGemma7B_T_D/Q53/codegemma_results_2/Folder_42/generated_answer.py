def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    text_len = len(text)
    for i in range(text_len - 43):
        for j in range(i + 44, text_len + 1):
            if text[i:j] == text[j - 1:i - 1:-1]:
                result.add(text[i:j])
    if not result:
        return set()
    else:
        return result