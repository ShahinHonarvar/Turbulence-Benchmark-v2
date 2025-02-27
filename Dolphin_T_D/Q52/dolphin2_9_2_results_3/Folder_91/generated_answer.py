def palindrome_of_length_n(string):
    string = string.lower()
    n = 7
    return set((s for s in (string[i:i + n] for i in range(len(string) - n + 1)) if s == s[::-1] and s.isalpha()))