def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 50):
        for j in range(i + 51, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result