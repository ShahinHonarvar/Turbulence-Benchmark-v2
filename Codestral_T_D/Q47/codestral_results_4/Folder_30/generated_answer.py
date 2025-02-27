def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(55, 72):
        for i in range(14, 91 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes