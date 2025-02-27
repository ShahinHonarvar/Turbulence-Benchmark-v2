def palindrome_of_length_at_least_n(text):
    result = set()
    text = text.lower()
    for length in range(144, len(text) + 1):
        for i in range(0, len(text) - length + 1):
            substring = text[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result