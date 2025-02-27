def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 18):
        palindrome = s[i:i + 19]
        if palindrome == palindrome[::-1]:
            result.add(palindrome)
    return result