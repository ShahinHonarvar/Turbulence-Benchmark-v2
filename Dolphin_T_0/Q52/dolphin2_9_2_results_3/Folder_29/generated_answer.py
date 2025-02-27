def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 18):
        if s[i:i + 19] == s[i:i + 19][::-1] and s[i:i + 19].isalpha():
            result.add(s[i:i + 19])
    return result