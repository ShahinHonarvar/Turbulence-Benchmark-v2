def palindrome_of_length_n(text):
    palindrome = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindrome.add(substring.lower())
    return palindrome