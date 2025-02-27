def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 93):
        substring = text[i:i + 94].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    for i in range(len(text) - 94, len(text)):
        substring = text[i:].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result