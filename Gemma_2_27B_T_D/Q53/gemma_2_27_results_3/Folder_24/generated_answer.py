def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 52):
        substring = text[i:i + 53]
        if substring.lower() == substring.lower()[::-1]:
            result.add(substring)
    return result