def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 52):
        if s[i:i + 53] == s[i:i + 53][::-1]:
            result.add(s[i:i + 53])
    return result