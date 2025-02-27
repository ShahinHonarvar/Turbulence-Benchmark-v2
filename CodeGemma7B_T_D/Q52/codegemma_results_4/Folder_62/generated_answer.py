def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text)):
        for j in range(i + 187, len(text) + 1):
            substring = text[i:j]
            if substring == substring.lower():
                result.add(substring)
    return result