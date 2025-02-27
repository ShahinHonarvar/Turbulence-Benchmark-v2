def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 72, len(s) + 1):
            substring = s[i:j]
            if all((char.isalpha() for char in substring)) and substring == substring[::-1]:
                res.add(substring)
    return res