def palindromes_of_specific_lengths(s):
    s = s[10:84]
    palindromes = set()
    for length in range(37, 61):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub == sub[::-1]:
                if sub.isalpha():
                    palindromes.add(sub.lower())
    return palindromes