def palindromes_of_specific_lengths(s):
    s = s[35:89].lower()
    palindromes = set()
    for length in range(24, 34):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes