def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 15):
        palindrome = s[i:i + 16]
        if palindrome == palindrome[::-1]:
            result.add(palindrome)
    return result