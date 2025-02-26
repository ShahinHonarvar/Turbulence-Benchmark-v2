def palindromes_of_specific_lengths(s):
    if len(s) <= 8:
        s = s.lower()
    else:
        s = s[1:9].lower()
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes