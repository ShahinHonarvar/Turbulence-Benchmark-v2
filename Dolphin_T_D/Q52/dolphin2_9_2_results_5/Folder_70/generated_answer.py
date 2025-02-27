def palindrome_of_length_n(s):
    s = s.lower()
    return set((s[i:j + 401] for i, j in zip(range(len(s) - 400), range(401, len(s))) if s[i:j + 401] == s[i:j + 401][::-1] and s[i:j + 401].isalpha()))