def palindromes_of_specific_lengths(s):
    substring = s[130:296]
    substring = ''.join((c for c in substring if c.isalpha() and c.isascii()))
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].lower() == substring[i:i + length][::-1].lower():
                palindromes.add(substring[i:i + length])
    return palindromes