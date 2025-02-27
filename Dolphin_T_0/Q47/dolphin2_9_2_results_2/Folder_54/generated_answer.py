def palindromes_of_specific_lengths(s):
    sub = s[27:78]
    palindromes = set()
    for i in range(len(sub)):
        for j in range(i + 18, len(sub) + 1):
            subs = sub[i:j]
            if subs == subs[::-1]:
                if subs.isalpha():
                    palindromes.add(subs.lower())
    return palindromes