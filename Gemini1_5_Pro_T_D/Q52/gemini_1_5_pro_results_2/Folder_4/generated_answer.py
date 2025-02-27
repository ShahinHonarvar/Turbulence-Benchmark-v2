def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 14):
        substring = text[i:i + 15]
        if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result