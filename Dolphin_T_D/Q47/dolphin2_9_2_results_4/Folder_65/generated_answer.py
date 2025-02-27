def palindromes_of_specific_lengths(s):
    substring = s[15:96]
    palindromes_set = set()
    for length in range(20, 67):
        for i in range(len(substring) - length + 1):
            sub_str = substring[i:i + length]
            if all((c.isalpha() for c in sub_str)) and sub_str.lower() == sub_str[::-1].lower():
                palindromes_set.add(sub_str)
    return palindromes_set