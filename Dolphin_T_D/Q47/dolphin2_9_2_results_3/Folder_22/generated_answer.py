def palindromes_of_specific_lengths(s):
    s = s[100:201]
    palindromes = set()
    for length in range(5, 11):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs.lower() and subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes