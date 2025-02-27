def palindrome_of_length_at_least_n(text):
    text_lower = text.lower()
    palindrome_set = set()
    text_len = len(text)
    for start_index in range(text_len):
        for end_index in range(start_index + 45, text_len + 1):
            substring = text_lower[start_index:end_index]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set