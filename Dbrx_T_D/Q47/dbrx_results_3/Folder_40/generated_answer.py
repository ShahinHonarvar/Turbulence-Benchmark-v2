def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring[0] in 'abcdefghijklmnopqrstuvwxyz' and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes