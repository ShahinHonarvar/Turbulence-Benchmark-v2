def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return set((s[i:i + 276] for i in range(len(s) - 275) if s[i:i + 276] == s[i:i + 276][::-1]))