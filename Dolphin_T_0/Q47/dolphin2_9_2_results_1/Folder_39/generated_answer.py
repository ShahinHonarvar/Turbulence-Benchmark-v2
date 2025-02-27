def palindromes_of_specific_lengths(s):
    s = s[31:92]
    palindromes = set()
    for length in range(50, 54):
        for index in range(len(s) - length + 1):
            substring = s[index:index + length]
            if all((c.isalpha() for c in substring)) and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes