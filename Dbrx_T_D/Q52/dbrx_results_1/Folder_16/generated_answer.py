def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 255 + 1):
        palindrome = s[i:i + 255]
        if palindrome.lower() == palindrome.lower()[::-1] and palindrome.isalpha():
            result.add(palindrome)
    return result