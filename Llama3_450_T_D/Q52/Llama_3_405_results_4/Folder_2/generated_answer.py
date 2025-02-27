def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return set((s[i:i + 147] for i in range(len(s) - 146) if s[i:i + 147] == s[i:i + 147][::-1]))