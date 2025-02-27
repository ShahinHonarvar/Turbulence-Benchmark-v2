def palindromes_of_specific_lengths(s):
    s = s[26:96]
    palindromes = set()
    for length in range(49, 52):
        for i in range(len(s) - length + 1):
            sub_s = s[i:i + length]
            if all((c.isalpha() for c in sub_s.lower())):
                if sub_s.lower() == sub_s.lower()[::-1]:
                    palindromes.add(sub_s)
    return palindromes