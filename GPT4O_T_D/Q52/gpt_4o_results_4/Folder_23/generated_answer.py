def palindrome_of_length_n(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    result = set()
    for i in range(len(s) - 68):
        substring = s[i:i + 69]
        if substring == substring[::-1]:
            result.add(substring)
    return result