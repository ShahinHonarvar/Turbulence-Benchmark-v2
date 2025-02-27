def palindrome_of_length_n(s):
    n = 255
    s = ''.join((c for c in s if c.isalpha())).lower()
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result