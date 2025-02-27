def palindromes_of_specific_lengths(s):
    s = s[11:84]
    palindromes = set()
    for length in range(13, 67):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs.isalpha() and subs.lower() == subs[::-1].lower():
                palindromes.add(subs)
    return palindromes