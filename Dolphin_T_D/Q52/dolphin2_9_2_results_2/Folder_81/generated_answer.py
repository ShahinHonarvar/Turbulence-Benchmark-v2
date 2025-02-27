def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    length = 99
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            result.add(substring)
    return result