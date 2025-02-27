def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 130):
        subStr = s[i:i + 131]
        if subStr == subStr[::-1] and subStr.isalpha():
            res.add(subStr)
    return res