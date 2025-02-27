def palindromes_of_specific_lengths(s):
    sub = s[10:56]
    palindromes = set()
    for length in range(3, 8):
        for i in range(len(sub) - length + 1):
            subs = sub[i:i + length].lower()
            if subs == subs[::-1]:
                if subs.isalpha():
                    palindromes.add(subs)
    return palindromes