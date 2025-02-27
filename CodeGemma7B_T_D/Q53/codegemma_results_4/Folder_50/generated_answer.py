def palindrome_of_length_at_least_n(text):
    text = text.lower()
    result = set()
    text_len = len(text)
    if text_len < 91:
        return result
    for i in range(text_len - 91 + 1):
        for j in range(i + 91, text_len + 1):
            palindrome = text[i:j]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result