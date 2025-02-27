def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        if len(s) - i >= 20 and s[i:i + 20] == s[i:i + 20][::-1]:
            result.add(s[i:i + 20])
    return result