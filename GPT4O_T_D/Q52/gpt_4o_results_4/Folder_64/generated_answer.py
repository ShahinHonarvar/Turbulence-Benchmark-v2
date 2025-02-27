def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    n = len(s)
    for i in range(n - 8):
        substring = s[i:i + 9]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result