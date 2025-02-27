def palindromes_of_specific_lengths(s):
    s = s[41:90]
    pal = set()
    for length in range(23, 39):
        for index in range(len(s) - length + 1):
            substr = s[index:index + length]
            if substr == substr[::-1]:
                pal.add(substr.lower())
    return pal