def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 87):
        substring = text[i:i + 88]
        if len(substring) == 88 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result