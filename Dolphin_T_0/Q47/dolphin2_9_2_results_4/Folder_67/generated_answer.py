def palindromes_of_specific_lengths(s):
    s = s[65:100]
    palindromes = set()
    for length in range(26, 34):
        for i in range(len(s) - length + 1):
            tmp = s[i:i + length]
            if tmp == tmp[::-1] and all((c.isalpha() for c in tmp)):
                palindromes.add(tmp.lower())
    return palindromes