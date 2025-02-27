def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(20, 31):
        for i in range(31 - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes