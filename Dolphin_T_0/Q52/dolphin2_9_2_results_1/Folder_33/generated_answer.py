def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        if len(s[i:]) >= 475:
            substring = s[i:i + 475]
            if substring == substring[::-1]:
                result.add(substring)
    return result