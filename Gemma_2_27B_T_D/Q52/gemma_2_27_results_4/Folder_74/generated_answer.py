def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 95):
        substring = text[i:i + 96].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result