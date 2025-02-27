def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 83):
        substring = text[i:i + 84]
        if len(substring) != 84:
            continue
        if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result