def palindromes_of_specific_lengths(s):
    s = s[31:71]
    palindromes = set()
    for i in range(len(s) - 20):
        for j in range(21, 33):
            subs = s[i:i + j]
            if subs == subs[::-1] and subs.isalpha():
                palindromes.add(subs.lower())
    return palindromes