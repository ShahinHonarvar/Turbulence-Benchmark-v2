def palindromes_of_specific_lengths(s):
    s = s[75:96].lower()
    lengths = [7, 8, 9]
    palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes