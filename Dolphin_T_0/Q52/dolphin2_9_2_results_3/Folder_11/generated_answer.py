def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    length = 77
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(substring) == length and substring == substring[::-1]:
                result.add(substring)
    return result