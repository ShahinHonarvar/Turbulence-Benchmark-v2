def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 41):
        substring = text[i:i + 42].lower()
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result