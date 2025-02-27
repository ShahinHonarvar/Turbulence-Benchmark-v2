def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text)):
        for j in range(i + 137, len(text) + 1):
            substring = text[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                result.add(substring)
    return result