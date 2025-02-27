def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for i in range(n - 28):
        substring = s[i:i + 29]
        if substring == substring[::-1]:
            result.add(substring)
    return result