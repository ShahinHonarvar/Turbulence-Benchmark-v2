def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 38):
        for j in range(i + 2, len(text)):
            substring = text[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    if not result:
        return set()
    return result