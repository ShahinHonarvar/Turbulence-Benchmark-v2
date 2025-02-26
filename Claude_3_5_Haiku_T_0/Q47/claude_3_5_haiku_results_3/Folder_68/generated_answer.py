def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for start in range(51):
        for length in range(50, 101):
            if start + length > 51:
                break
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes