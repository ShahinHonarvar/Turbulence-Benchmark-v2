def palindromes_of_specific_lengths(s):
    sub_s = s[:6]
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(sub_s) - length + 1):
            sub = sub_s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(''.join((c.lower() for c in sub)))
    return palindromes