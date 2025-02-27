def palindrome_of_length_at_least_n(text):
    result = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 149, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result