def palindromes_of_specific_lengths(s):
    s = s[11:94]
    palindromes = set()
    for length in range(34, 55):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes