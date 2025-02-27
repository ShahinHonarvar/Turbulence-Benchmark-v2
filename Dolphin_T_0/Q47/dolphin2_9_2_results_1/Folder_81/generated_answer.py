def palindromes_of_specific_lengths(s):
    substring = s[12:123]
    palindromes = set()
    for length in range(12, 221):
        for i in range(len(substring) - length + 1):
            sub_s = substring[i:i + length]
            if sub_s.lower() == sub_s[::-1].lower():
                palindromes.add(sub_s)
    return palindromes