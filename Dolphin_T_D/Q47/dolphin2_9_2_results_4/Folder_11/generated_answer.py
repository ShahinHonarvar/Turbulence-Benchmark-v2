def palindromes_of_specific_lengths(s):
    s = s[24:98]
    palindromes = set()
    for i in range(len(s)):
        for j in range(len(s[i:]), 10):
            sub = s[i:i + j]
            if sub == sub[::-1] and all((x.isalpha() for x in sub)):
                palindromes.add(sub.lower())
    return palindromes