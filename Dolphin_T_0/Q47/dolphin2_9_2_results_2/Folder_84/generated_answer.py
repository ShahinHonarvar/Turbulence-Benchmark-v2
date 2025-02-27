def palindromes_of_specific_lengths(s):
    substring = s[23:78]
    palindromes = set()
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            if all((c.isalpha() for c in substring[i:i + length])) and substring[i:i + length].lower() == substring[i:i + length][::-1].lower():
                palindromes.add(substring[i:i + length])
    return palindromes