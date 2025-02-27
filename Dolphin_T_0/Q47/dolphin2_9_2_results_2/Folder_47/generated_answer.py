def palindromes_of_specific_lengths(s):
    s = s[39:95]
    palindromes = set()
    for len_ in range(14, 53):
        for i in range(len(s) - len_ + 1):
            subs = s[i:i + len_]
            if subs.lower() == subs[::-1].lower():
                palindromes.add(subs)
    return palindromes