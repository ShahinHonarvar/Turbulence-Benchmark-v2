def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindrome_set = set()
    for i in range(len(text) - 2):
        for j in range(i + 2, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 30:
                palindrome_set.add(substring)
    return palindrome_set