def palindrome_of_length_n(s):
    s = s.lower()
    return {s[i:i + 10] for i in range(len(s) - 9) if s[i:i + 10] == s[i:i + 10][::-1] and s[i:i + 10].isalpha()}