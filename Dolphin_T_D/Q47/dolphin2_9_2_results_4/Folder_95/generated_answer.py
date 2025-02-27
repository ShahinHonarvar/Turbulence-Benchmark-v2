def palindromes_of_specific_lengths(s):
    s = s[11:57]
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes