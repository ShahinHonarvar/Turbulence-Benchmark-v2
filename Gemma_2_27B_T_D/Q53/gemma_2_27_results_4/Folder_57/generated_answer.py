def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 92):
        for j in range(i + 92, len(text)):
            substring = text[i:j + 1]
            if substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result