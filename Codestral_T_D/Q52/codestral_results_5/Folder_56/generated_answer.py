def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 95] for i in range(len(s) - 94) if s[i:i + 95] == s[i:i + 95][::-1]}