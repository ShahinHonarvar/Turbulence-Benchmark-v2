def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 12):
        for j in range(i + 12, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result