def palindromes_of_specific_lengths(s):
    if len(s) < 10:
        s = s + ' ' * (10 - len(s))
    s = s[:10]
    palindromes = set()
    for length in range(3, 6):
        for start in range(11 - length):
            substring = s[start:start + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes