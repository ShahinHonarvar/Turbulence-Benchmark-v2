def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        if len(s[i:]) >= 45:
            for j in range(22, 46):
                if s[i:i + j] == s[i:i + j][::-1]:
                    result.add(s[i:i + j])
                    break
    return result