def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 43):
        for j in range(i + 44, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
                result.add(substring)
    return result