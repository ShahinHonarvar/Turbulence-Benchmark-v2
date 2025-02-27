def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 100] for i in range(len(s) - 99) if s[i:i + 100] == s[i:i + 100][::-1] and s[i:i + 100].isalpha()}