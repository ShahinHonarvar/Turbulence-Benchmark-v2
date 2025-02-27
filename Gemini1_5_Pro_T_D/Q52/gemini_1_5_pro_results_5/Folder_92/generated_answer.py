def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 9):
        substring = text[i:i + 10].lower()
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result