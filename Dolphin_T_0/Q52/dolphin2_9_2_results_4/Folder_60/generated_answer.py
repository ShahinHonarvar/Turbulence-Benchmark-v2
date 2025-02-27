def palindrome_of_length_n(s, n=88):
    if not isinstance(s, str) or not isinstance(n, int):
        raise TypeError('The function takes one argument, a string, and an integer.')
    if n <= 0:
        raise ValueError('The length of the palindrome should be a positive integer.')
    s = s.lower()
    return set((s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n] == s[i:i + n][::-1]))