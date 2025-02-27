def palindrome_of_length_n(s):
    s = s.lower()
    length = 67
    result = set()
    for i in range(len(s)):
        if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
            result.add(s[i:i + length])
    return result