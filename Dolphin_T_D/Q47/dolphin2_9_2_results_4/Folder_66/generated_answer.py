def palindromes_of_specific_lengths(s):
    s = s[32:80]
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(s) - length + 1):
            subsring = s[i:i + length]
            if all((c.isalpha() for c in subsring)) and subsring.lower() == subsring[::-1].lower():
                palindromes.add(subsring)
    return palindromes