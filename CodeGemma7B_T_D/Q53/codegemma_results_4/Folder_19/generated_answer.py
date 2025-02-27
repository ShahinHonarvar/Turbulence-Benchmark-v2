def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    if len(text) < 23:
        return result
    for i in range(len(text) - 22):
        for j in range(i + 23, len(text) + 1):
            if text[i:j] == text[i:j][::-1]:
                result.add(text[i:j])
    return result