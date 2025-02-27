def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(29, 63):
        for i in range(11, len(s) - length + 1):
            substring = s[i:i + length]
            if substring.upper() == ''.join(reversed(substring.upper())) and substring.isalpha():
                palindromes.add(substring)
    return palindromes