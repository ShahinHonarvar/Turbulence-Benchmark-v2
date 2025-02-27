def palindromes_of_specific_lengths(s):
    sub_s = s[43:96] + s[43:95]
    palindromes = set()
    for i in range(18, 48):
        for j in range(i):
            if sub_s[j:j + i].lower() == sub_s[j:j + i].lower()[::-1]:
                palindromes.add(sub_s[j:j + i])
    return palindromes