def palindrome_of_length_n(s):
    s = s.lower()
    length = 76
    return set([s[i:i + length] for i in range(len(s) - length + 1) if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha()])