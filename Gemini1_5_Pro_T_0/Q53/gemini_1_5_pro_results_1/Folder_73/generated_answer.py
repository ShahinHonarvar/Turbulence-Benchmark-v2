def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text)):
        for j in range(i + 94, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                result.add(substring)
    return result