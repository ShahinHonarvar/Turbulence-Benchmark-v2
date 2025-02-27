def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    palindromes = set()
    for length in range(136, 161):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs.isalpha() and subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes