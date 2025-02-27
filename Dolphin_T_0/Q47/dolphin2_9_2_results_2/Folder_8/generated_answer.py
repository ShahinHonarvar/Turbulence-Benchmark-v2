def palindromes_of_specific_lengths(s):
    s = s[16:73]
    palindromes = set()
    for i in range(len(s) - 49):
        subs = s[i:i + 50]
        if subs == subs[::-1] and subs.isalpha():
            palindromes.add(subs)
    for i in range(len(s) - 49):
        subs = s[i:i + 51]
        if subs == subs[::-1] and subs.isalpha():
            palindromes.add(subs)
    return palindromes