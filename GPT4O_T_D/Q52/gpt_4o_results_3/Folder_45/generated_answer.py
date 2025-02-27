def palindrome_of_length_n(s):
    n = 21
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result