def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 29):
        for j in range(i + 30, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result