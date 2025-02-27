def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindrome_set = set()
    for length in range(95, len(text) + 1):
        for i in range(len(text) - length + 1):
            substring = text[i:i + length]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set