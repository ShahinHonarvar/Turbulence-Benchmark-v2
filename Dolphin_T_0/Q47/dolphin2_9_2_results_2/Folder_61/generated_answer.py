def palindromes_of_specific_lengths(s):
    s = s[:31]
    palindromes = set()
    for length in range(20, 31):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs.lower():
                if subs == subs[::-1]:
                    palindromes.add(subs)
    return palindromes