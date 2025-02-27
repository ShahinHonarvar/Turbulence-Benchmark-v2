def palindrome_of_length_n(text):
    palindrome_set = set()
    text = text.lower()
    for i in range(len(text) - 94 + 1):
        for j in range(i + 94, len(text) + 1):
            substring = text[i:j]
            rsubstring = substring[::-1]
            if substring == rsubstring:
                palindrome_set.add(substring)
    return palindrome_set