def palindrome_of_length_n(s):
    n = 94
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result