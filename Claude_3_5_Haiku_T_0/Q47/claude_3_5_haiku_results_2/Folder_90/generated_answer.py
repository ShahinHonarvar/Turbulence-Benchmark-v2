def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for start in range(106, 281 - 135):
        for length in range(136, 152):
            substring = s[start:start + length]
            if len(substring) == length and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes