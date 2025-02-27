def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return {s[i:i + 87] for i in range(len(s) - 86) if s[i:i + 87] == s[i:i + 87][::-1]}