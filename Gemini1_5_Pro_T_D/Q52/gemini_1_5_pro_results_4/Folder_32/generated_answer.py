def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 112):
        substring = text[i:i + 113].lower()
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result