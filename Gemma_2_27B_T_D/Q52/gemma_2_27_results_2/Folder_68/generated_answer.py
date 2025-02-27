def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 75):
        substring = text[i:i + 76].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(text[i:i + 76])
    return result