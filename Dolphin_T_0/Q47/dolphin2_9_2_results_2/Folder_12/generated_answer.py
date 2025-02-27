def palindromes_of_specific_lengths(s):
    substring = s[62:89]
    lengths = [i for i in range(18, 22)]
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].replace(' ', '').lower() == substring[i:i + length].replace(' ', '').lower()[::-1] and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes