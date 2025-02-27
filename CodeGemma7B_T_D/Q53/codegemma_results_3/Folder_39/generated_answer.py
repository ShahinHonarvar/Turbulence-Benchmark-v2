def palindrome_of_length_at_least_n(text):
    alphanumeric_text = ''.join((c.lower() for c in text if c.isalnum()))
    palindrome_set = set()
    for i in range(len(alphanumeric_text) - 68):
        substring = alphanumeric_text[i:i + 69]
        if substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set