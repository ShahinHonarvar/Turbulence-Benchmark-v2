def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(3, 11):
        for start in range(1, 300):
            end = start + length
            if end > len(s):
                break
            substring = s[start:end]
            if all((char.isalpha() for char in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes