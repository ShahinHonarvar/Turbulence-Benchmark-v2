def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 83):
        substring = text[i:i + 84]
        if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result