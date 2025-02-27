def palindromes_of_specific_lengths(s):
    substring = s[29:99]
    palindromes = set()
    for length in range(6, 10):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub.lower() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes