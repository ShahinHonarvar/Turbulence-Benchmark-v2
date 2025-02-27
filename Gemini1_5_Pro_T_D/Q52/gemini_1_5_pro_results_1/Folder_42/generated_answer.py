def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 278):
        substring = text[i:i + 279]
        if len(substring) == 279 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result