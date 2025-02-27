def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 5):
        substring = text[i:i + 6].lower()
        if substring == substring[::-1]:
            result.add(substring)
    return result