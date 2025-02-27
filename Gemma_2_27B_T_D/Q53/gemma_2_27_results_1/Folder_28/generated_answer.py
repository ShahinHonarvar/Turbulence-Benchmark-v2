def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 41):
        substring = text[i:i + 42].lower()
        if substring == substring[::-1]:
            result.add(substring)
    for i in range(len(text) - 42):
        substring = text[i:i + 43].lower()
        if substring == substring[::-1]:
            result.add(substring)
    return result