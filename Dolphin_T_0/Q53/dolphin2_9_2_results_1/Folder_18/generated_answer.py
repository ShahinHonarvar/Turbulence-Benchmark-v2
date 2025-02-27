def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    length = len(s)
    for i in range(length):
        for j in range(i, length):
            substring = s[i:j + 1]
            if len(substring) >= 62:
                if substring == substring[::-1]:
                    result.add(substring)
    return result