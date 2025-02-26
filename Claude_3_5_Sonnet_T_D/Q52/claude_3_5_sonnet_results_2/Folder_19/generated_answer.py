def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    result = set()
    for i in range(n - 66):
        substring = s[i:i + 67]
        if substring == substring[::-1]:
            result.add(substring)
    return result