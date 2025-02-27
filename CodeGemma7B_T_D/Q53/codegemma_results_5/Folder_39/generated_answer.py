def palindrome_of_length_at_least_n(text):
    result = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            palindrome = substring[::-1]
            if palindrome == substring and len(palindrome) >= 69:
                result.add(palindrome)
    return result