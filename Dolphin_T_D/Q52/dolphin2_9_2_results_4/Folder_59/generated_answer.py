def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 38):
        if s[i:i + 39] == s[i:i + 39][::-1]:
            result.add(s[i:i + 39])
    return result