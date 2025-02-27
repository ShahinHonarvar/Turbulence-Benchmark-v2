def palindromes_of_specific_lengths(s):
    sub_s = s[30:85]
    palindromes = set()
    for i in range(len(sub_s)):
        for j in range(i + 12, min(len(sub_s) + 1, i + 21)):
            sub_s2 = sub_s[i:j]
            if all((c.isalpha() for c in sub_s2)):
                if sub_s2.lower() == sub_s2.lower()[::-1]:
                    palindromes.add(sub_s2)
    return palindromes