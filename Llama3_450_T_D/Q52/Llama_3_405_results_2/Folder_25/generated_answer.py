def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 90] for i in range(len(s) - 89) if s[i:i + 90] == s[i:i + 90][::-1] and s[i:i + 90].isalpha()}