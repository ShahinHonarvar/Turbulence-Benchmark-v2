def palindrome_of_length_n(s):
    return set((i for i in [s[x:x + 37].lower() for x in range(len(s) - 36)] if i == i[::-1] and i.isalpha()))