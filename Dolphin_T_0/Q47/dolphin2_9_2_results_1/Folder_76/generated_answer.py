def palindromes_of_specific_lengths(s):
    substring = s[101:293]
    palindromes = set()
    for length in range(154, 183):
        for i in range(len(substring)):
            if substring[i:i + length] == substring[i:i + length][::-1].lower() and substring[i:i + length].isalpha():
                palindromes.add(substring[i:i + length])
    return palindromes