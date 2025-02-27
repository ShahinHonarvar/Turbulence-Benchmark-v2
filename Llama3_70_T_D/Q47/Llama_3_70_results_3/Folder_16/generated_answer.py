def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(15, 87 - 50):
        for length in range(51, 61):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes