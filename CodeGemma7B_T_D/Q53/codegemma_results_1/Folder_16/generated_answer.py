def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindrome_set = set()
    for i in range(len(text)):
        for j in range(119, len(text) - i + 1):
            palindrome = text[i:i + j]
            if palindrome == palindrome[::-1]:
                palindrome_set.add(palindrome)
    return palindrome_set