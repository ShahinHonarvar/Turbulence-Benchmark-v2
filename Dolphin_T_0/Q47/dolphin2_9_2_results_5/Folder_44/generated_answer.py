def palindromes_of_specific_lengths(s):
    sub_s = s[17:99]
    lengths = range(31, 52)
    palindromes = set()
    for l in lengths:
        for i in range(len(sub_s) - l + 1):
            subs = sub_s[i:i + l]
            if subs == subs[::-1] and subs.isalpha():
                palindromes.add(subs.lower())
    return palindromes