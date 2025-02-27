def palindrome_of_length_at_least_n(text):
    palindrome_set = set()
    reversed_text = text[::-1]
    for i in range(len(text)):
        for j in range(i + 26, len(text) + 1):
            substring = text[i:j]
            if substring == reversed_text[i:j]:
                palindrome_set.add(substring)
    return palindrome_set