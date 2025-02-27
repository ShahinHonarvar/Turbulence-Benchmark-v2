def palindrome_of_length_n(s):
    s = s.lower()
    return set((sub for i in range(len(s)) for sub in [s[i:i + 279]] if sub == sub[::-1] and sub.isalpha()))