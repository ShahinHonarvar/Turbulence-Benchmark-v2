def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(13, 43):
        for i in range(44, 100 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes