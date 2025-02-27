def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            result.add(s[i:i + 3])
    return result