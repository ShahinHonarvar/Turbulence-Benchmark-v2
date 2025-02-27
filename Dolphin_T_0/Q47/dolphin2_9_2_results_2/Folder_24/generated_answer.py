def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i, min(i + 78, 93)):
            subs = s[i:j + 1]
            if subs == subs[::-1] and 42 <= len(subs) <= 77:
                palindromes.add(''.join(filter(str.isalpha, subs.lower())))
    return palindromes