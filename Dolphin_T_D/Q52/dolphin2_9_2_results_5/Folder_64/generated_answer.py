def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 9] for i in range(len(s) - 9) if s[i:i + 9] == s[i:i + 9][::-1]}