def palindromes_of_specific_lengths(s):
    s = s[17:96]
    palindromes = set()
    for length in range(13, 50):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes