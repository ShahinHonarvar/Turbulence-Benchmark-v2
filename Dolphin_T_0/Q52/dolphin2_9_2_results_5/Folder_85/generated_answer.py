def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 45):
        if s[i:i + 46] == s[i:i + 46][::-1] and s[i:i + 46].isalpha():
            result.add(s[i:i + 46])
    return result