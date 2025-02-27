def palindromes_of_specific_lengths(s):
    substring = s[2:9]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(substring) + 1 - length):
            subs = substring[i:i + length]
            if subs == subs[::-1] and all((c.isalpha() for c in subs)):
                palindromes.add(subs.lower())
    return palindromes