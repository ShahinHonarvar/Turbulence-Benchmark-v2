def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return {s[i:i + 39] for i in range(len(s) - 38) if s[i:i + 39] == s[i:i + 39][::-1]}