def palindrome_of_length_n(string, n=87, _sorted=lambda x: '-'.join(x)):
    """
    Return a set of all palindromes of the specified length n as substrings of the input string.
    The palindromes should consist only of English letters and should be found in a case-insensitive manner.
    If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set.
    """
    string = ''.join((c.lower() for c in string if c.isalpha()))
    if n % 2 == 1:
        return set((p for p in {string[i:i + n] for i in range(len(string) - n + 1)} if p == p[::-1] and p[::n / 2] != p[::n / 2][::-1]))
    else:
        return set((p + q[::-1] for p, q in zip(string, string[::-1])[-(n / 2):] if p != q and p == q.lower() and (p[::n / 2] != p[::n / 2][::-1])))