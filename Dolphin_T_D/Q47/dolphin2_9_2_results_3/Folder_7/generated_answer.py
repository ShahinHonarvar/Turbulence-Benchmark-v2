def palindromes_of_specific_lengths(s):
    substring = s[119:257]
    palindromes = set()
    for length in range(104, 124):
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub.lower() and sub[::-1].lower() == sub:
                palindromes.add(sub)
    return palindromes