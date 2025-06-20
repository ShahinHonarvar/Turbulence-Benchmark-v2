def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    result = set()
    for i in range(len(s) - 20):
        substring = s[i:i + 21]
        if substring == substring[::-1]:
            result.add(substring)
    return result