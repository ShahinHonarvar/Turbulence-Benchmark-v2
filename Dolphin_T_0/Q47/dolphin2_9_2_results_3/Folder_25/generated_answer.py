def palindromes_of_specific_lengths(s):
    s = s[25:85]
    pal = set()
    for len_ in range(30, 47):
        for i in range(len_ - 1, len(s)):
            if s[i - len_ + 1:i + 1].lower() == s[i - len_ + 1:i + 1].lower()[::-1]:
                pal.add(s[i - len_ + 1:i + 1])
    return pal