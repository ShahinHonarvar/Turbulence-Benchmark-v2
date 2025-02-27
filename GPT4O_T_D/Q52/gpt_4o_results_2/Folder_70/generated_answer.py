def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    length = len(s)
    for i in range(length - 400):
        substring = s[i:i + 401]
        if substring == substring[::-1]:
            result.add(substring)
    return result