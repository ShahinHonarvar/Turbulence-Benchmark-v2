def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[100:201]
    for length in range(5, 11):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes