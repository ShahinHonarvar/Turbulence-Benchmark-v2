def palindromes_of_specific_lengths(s):
    s = s[10:97]
    palindromes = set()
    for length in range(45, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes