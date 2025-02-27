def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 8):
        if s[i:i + 9] == s[i:i + 9][::-1]:
            result.add(s[i:i + 9])
    return result