def palindromes_of_specific_lengths(s):
    index_range = s[15:77]
    palindromes = set()
    for i in range(43, 48):
        for j in range(0, len(index_range) - i + 1):
            subs = index_range[j:j + i]
            if subs == subs[::-1] and subs.isalpha():
                palindromes.add(subs.lower())
    return palindromes