def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 146):
        if s[i:i + 147] == s[i:i + 147][::-1]:
            result.add(s[i:i + 147])
    return result