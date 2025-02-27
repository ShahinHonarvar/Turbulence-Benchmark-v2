def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    if len(s) < 91:
        return set()
    result = set()
    for i in range(len(s) - 91 + 1):
        if s[i:i + 91] == s[i:i + 91][::-1]:
            result.add(s[i:i + 91])
    return result