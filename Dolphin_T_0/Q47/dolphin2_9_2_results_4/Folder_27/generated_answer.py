def palindromes_of_specific_lengths(s):
    s = s[13:100]
    palindromes = set()
    for length in range(26, 30):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes