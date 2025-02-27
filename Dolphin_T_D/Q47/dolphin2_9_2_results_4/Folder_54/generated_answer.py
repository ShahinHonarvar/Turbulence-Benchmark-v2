def palindromes_of_specific_lengths(s):
    s = s[27:78]
    palindromes = set()
    for length in range(18, 20):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs == subs[::-1]:
                if subs.isalpha():
                    palindromes.add(subs.lower())
    return palindromes