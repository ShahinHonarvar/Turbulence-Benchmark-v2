def palindromes_of_specific_lengths(s):
    s = s[10:83]
    r = set()
    for length in range(13, 67):
        for i in range(len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1] and s[i:i + length].isalpha():
                r.add(s[i:i + length])
    return r