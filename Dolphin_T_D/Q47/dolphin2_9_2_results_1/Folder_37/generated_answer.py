def palindromes_of_specific_lengths(s):
    pals = set()
    for i in range(10):
        for j in range(i + 3, min(i + 6, 10)):
            part = s[i:j + 1]
            part = ''.join((c for c in part if c.isalpha()))
            part = part.lower()
            if part == part[::-1]:
                pals.add(part)
    return pals