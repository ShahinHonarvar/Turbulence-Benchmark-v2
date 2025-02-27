def palindromes_of_specific_lengths(s):
    s = s[12:100].lower()
    pal = set()
    for length in range(26, 30):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                pal.add(substr)
    return pal