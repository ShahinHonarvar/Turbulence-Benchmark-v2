def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for start in range(15, 87):
        for length in range(51, 61):
            end = start + length
            if end > len(s):
                break
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes