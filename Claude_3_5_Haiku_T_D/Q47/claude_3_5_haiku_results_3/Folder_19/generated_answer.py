def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for start in range(10, 56):
        for length in range(3, 8):
            end = start + length
            if end > len(s):
                break
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes