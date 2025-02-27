def palindromes_of_specific_lengths(s):
    substring = s[10:56]
    palindromes = set()
    for length in range(3, 8):
        for i in range(len(substring)):
            sub = substring[i:i + length]
            if sub == sub.lower() and sub[::-1] == sub:
                palindromes.add(sub)
    return palindromes