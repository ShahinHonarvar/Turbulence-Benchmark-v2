def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 40):
        if s[i:i + 40] == s[i:i + 40][::-1] and s[i:i + 40].isalpha():
            result.add(s[i:i + 40])
    return result