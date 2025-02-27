def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 5):
        substring = text[i:i + 6]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            result.add(substring.lower())
    return result