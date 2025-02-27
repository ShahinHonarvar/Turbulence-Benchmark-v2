def palindrome_of_length_n(s):
    res = set()
    s = s.lower()
    if len(s) < 318:
        return res
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1]:
                res.add(palindrome)
    return res