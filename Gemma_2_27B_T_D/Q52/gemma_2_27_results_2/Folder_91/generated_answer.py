def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 6):
        substring = text[i:i + 7].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(text[i:i + 7])
    return result