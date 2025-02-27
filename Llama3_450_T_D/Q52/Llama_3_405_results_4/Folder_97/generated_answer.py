def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return {s[i:i + 210] for i in range(len(s) - 209) if s[i:i + 210] == s[i:i + 210][::-1]}