def palindromes_of_specific_lengths(s):
    substring = s[12:100]
    lengths = range(26, 30)
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].lower() == substring[i:i + length].lower()[::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindrom