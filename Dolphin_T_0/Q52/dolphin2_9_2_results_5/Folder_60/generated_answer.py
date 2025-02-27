def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 88
    return set([s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n] == s[i:i + n][::-1]])