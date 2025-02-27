def palindromes_of_specific_lengths(s):
    substring = s[200:301]
    substring = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length])
    return palindromes