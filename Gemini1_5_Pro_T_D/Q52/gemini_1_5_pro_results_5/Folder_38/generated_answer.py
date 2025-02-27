def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 37):
        substring = text[i:i + 38].lower()
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result