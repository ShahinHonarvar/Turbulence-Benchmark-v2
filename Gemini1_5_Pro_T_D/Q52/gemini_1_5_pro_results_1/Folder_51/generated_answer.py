def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 72):
        substring = text[i:i + 73]
        if len(substring) == 73 and substring.lower() == substring[::-1].lower() and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result