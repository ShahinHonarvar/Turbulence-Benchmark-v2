def palindrome_of_length_at_least_n(text):
    palindrome_set = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 40, len(text)):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                palindrome_set.add(text[i:j + 1])
    return palindrome_set