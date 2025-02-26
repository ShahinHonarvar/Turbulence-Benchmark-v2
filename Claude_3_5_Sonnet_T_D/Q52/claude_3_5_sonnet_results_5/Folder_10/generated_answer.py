def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    result = set()
    for i in range(len(s) - 53):
        substr = s[i:i + 54]
        if substr == substr[::-1]:
            result.add(substr)
    return result