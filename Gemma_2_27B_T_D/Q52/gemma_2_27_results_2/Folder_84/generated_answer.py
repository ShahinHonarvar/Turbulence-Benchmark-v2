def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 130):
        substring = text[i:i + 131].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result