def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 59):
        for j in range(i + 60, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                result.add(substring)
    return result