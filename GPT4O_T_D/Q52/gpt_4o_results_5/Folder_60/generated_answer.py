def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = len(s)
    length = 88
    if length > n:
        return result
    for i in range(n - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            result.add(s[i:i + length])
    return result