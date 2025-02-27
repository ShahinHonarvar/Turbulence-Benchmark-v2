def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 76):
        substring = text[i:i + 77].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(text[i:i + 77])
    return result