def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 90 + 1):
        if s[i:i + 90] == s[i:i + 90][::-1]:
            result.add(s[i:i + 90])
    return result