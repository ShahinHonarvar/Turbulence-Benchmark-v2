def palindromes_of_specific_lengths(s):
    s = s[200:301]
    palindromes = set()
    for i in range(10, 51):
        for j in range(len(s) - i + 1):
            subs = s[j:j + i]
            if subs == subs[::-1] and all((char.isalpha() for char in subs)):
                palindromes.add(subs.lower())
    return palindromes