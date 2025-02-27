def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 25):
        palindrome = text[i:i + 26]
        if palindrome == palindrome[::-1]:
            result.add(palindrome)
    return result