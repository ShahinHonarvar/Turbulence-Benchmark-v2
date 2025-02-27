def palindromes_of_specific_lengths(s):
    s = s[69:141]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1] and all((char.isalpha() for char in subs)):
                palindromes.add(subs.lower())
    return palindromes