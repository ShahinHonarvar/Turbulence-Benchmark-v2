def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return {s[i:i + 94] for i in range(len(s) - 93) if s[i:i + 94] == s[i:i + 94][::-1]}