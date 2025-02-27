def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 87):
        substring = text[i:i + 88]
        if substring.lower() == substring.lower()[::-1]:
            result.add(substring)
    return result