def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for start in range(101, 293 - 153):
        for length in range(154, 183):
            substring = s[start:start + length]
            if len(substring) == length and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes