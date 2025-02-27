def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    result = set()
    for i in range(length - 58):
        substring = s[i:i + 59]
        if substring == substring[::-1]:
            result.add(substring)
    return result