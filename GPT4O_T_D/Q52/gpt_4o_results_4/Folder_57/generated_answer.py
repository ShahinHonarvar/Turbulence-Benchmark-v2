def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    for i in range(length - 91):
        substring = s[i:i + 92]
        if substring == substring[::-1]:
            result.add(substring)
    return result