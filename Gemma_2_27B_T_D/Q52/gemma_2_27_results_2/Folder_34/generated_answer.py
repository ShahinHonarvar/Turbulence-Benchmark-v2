def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 32):
        substring = text[i:i + 33].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(text[i:i + 33])
    return result