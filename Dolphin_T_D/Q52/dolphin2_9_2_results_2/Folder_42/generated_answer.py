def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 278):
        if s[i:i + 279] == s[i:i + 279][::-1]:
            result.add(s[i:i + 279])
    return result