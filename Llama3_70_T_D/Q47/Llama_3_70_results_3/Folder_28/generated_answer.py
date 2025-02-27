def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[32:72]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 21, min(i + 33, len(substring) + 1)):
            sub = substring[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes