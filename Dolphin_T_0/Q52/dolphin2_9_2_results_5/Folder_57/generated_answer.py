def palindrome_of_length_n(s):
    s_lower = s.lower()
    return {s[i:i + 92] for i in range(len(s_lower) - 91) if s[i:i + 92] == s[i:i + 92][::-1]}