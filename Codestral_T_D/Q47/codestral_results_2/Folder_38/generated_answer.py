def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(38, 61):
        for i in range(18, 87 - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes