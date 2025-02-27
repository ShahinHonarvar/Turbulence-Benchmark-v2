def palindrome_of_length_at_least_n(text):
    result = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 150, len(text) + 1):
            palindrome = text[i:j]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result