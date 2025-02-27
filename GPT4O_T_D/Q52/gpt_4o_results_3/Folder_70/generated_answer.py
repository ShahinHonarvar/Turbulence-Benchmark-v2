def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s.lower()))
    length = len(s)
    if length < 401:
        return result
    for i in range(length - 400):
        substring = s[i:i + 401]
        if substring == substring[::-1]:
            result.add(substring)
    return result