def palindrome_of_length_n(s):
    return set((substring for i in range(len(s) - 34) for substring in [s[i:i + 35]] if substring.lower() == substring[::-1].lower() and substring.isalpha()))