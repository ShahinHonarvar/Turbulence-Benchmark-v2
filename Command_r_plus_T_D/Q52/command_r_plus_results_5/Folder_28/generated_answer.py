def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    result = set()
    for i in range(length - 42):
        substring = s[i:i + 43]
        if substring == substring[::-1]:
            result.add(substring)
    return result