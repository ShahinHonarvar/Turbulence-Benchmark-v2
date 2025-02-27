def palindromes_of_specific_lengths(s):
    s = s[39:95]
    palindromes = set()
    for length in range(14, 53):
        for i in range(0, len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs[::-1] and subs.isalpha() and (subs.lower() == subs):
                palindromes.add(subs)
    return palindromes