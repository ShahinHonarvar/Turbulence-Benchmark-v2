def palindromes_of_specific_lengths(s):
    substring = s[124:283]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 108, len(substring)):
            subs = substring[i:j + 1]
            if subs == subs[::-1] and subs.isalpha() and (108 <= len(subs) <= 126):
                palindromes.add(subs.lower())
    return palindromes