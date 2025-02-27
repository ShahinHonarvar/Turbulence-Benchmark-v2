def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 40):
        substring = text[i:i + 41].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result