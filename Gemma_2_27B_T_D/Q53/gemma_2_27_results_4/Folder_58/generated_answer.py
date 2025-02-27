def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 146):
        substring = text[i:i + 147].lower()
        if substring == substring[::-1]:
            result.add(substring)
    return result