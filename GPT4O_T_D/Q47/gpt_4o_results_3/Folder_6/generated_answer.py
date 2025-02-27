def palindromes_of_specific_lengths(s):
    if len(s) < 99:
        return set()
    s = s[45:99]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(40, 48):
        for start in range(len(s) - length + 1):
            subs = s[start:start + length]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes