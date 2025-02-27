def palindromes_of_specific_lengths(s):
    s = s[29:97]
    palindromes = set()
    for i in range(12, 19):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes