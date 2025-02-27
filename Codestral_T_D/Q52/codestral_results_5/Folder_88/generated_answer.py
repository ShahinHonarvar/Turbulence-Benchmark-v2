def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 13] for i in range(len(s) - 13) if s[i:i + 13] == s[i:i + 13][::-1] and s[i:i + 13].isalpha()}