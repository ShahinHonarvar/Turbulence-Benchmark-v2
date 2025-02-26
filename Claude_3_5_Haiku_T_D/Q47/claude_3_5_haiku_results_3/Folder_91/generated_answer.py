def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(3, 6):
        for i in range(11 - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes