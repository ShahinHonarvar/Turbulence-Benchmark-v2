def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[:51]
    for length in range(50, 101):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes