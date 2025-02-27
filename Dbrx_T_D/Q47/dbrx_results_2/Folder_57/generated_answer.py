def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(16, 95):
        for length in range(39, 53):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes