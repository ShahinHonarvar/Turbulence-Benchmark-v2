def palindromes_of_specific_lengths(s):
    pal = set()
    s = s[29:97]
    for length in range(12, 19):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                pal.add(substring)
    return pal