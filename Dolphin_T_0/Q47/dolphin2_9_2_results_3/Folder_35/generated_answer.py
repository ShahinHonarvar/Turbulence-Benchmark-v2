def palindromes_of_specific_lengths(s):
    substring = s[34:91]
    palindromes = set()
    for length in range(14, 40):
        for i in range(0, len(substring) - length + 1):
            substring_check = substring[i:i + length]
            if substring_check.lower() == substring_check.lower()[::-1] and substring_check.isalpha():
                palindromes.add(substring_check)
    return palindromes