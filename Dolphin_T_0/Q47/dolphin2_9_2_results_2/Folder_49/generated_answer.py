def palindromes_of_specific_lengths(s):
    s = s[10:101]
    palindromes = set()
    for i in range(len(s) - 9):
        for j in range(i + 10, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1] and 10 <= len(subs) <= 50 and subs.isalpha():
                palindromes.add(subs.lower())
    return palindromes