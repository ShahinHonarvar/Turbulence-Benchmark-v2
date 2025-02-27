def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    for start in range(len(text)):
        for end in range(start + 26, len(text) + 1):
            if text[start:end] == text[start:end][::-1]:
                result.add(text[start:end])
    return result