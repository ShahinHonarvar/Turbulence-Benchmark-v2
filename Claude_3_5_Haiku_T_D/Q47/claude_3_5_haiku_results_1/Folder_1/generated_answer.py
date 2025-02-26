def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for start in range(15, 90 - 39):
        for length in range(40, 73):
            substring = s[start:start + length]
            if len(substring) == length and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes