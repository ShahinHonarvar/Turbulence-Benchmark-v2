def palindrome_of_length_at_least_n(text):
    results = set()
    length = 90
    text = text.lower()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) >= length:
                results.add(substring)
    return results