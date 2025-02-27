def palindromes_of_specific_lengths(s):
    s = s[130:296]
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and all((char.isalpha() for char in substring)):
                palindromes.add(substring.lower())
    return palindromes