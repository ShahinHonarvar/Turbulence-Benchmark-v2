def palindromes_of_specific_lengths(s):
    s = s[34:91]
    palindromes = set()
    for length in range(14, 40):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs.lower() == subs.lower()[::-1]:
                palindromes.add(subs)
    return palindromes