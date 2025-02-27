def palindromes_of_specific_lengths(s):
    s = s[s.index(s, 35):s.index(s, 89)]
    palindromes = set()
    for length in range(24, 34):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes