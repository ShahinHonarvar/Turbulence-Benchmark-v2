def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 8):
        substring = text[i:i + 9]
        if len(substring) == 9 and substring.lower() == substring.lower()[::-1] and substring.isalpha():
            result.add(substring.lower())
    return result