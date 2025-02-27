def palindromes_of_specific_lengths(s):
    substring = s[103:277]
    lengths = range(100, 170)
    palindromes = set()
    for length in lengths:
        for index in range(len(substring) - length + 1):
            sub_s = substring[index:index + length]
            if sub_s == sub_s[::-1] and sub_s.isalpha():
                palindromes.add(sub_s.lower())
                palindromes.add(sub_s.upper())
    return palindromes