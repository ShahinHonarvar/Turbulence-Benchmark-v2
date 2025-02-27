def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 94):
        substring = text[i:i + 95]
        if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result