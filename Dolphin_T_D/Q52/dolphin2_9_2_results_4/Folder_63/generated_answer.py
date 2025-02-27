def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 17):
        if s[i:i + 18] == s[i:i + 18][::-1] and s[i:i + 18].isalpha():
            result.add(s[i:i + 18])
    return result