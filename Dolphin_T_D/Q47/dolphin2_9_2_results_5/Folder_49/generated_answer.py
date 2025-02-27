def palindromes_of_specific_lengths(s):
    s = ''.join((c for c in s.lower() if c.isalpha()))
    pals = set()
    for i in range(len(s)):
        if 10 <= i <= 100:
            for j in range(i + 9, min(i + 51, len(s)) + 1):
                if s[i - 10:j] == s[i - 10:j][::-1]:
                    pals.add(s[i - 10:j])
    return pals