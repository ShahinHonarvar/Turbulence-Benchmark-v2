def palindromes_of_specific_lengths(s):
    substring = s[40:90]
    palindromes_set = set()
    for length in range(23, 39):
        for i in range(len(substring) - length + 1):
            sub_s = substring[i:i + length]
            if sub_s.lower() == sub_s.lower()[::-1]:
                palindromes_set.add(sub_s)
    return palindromes_set