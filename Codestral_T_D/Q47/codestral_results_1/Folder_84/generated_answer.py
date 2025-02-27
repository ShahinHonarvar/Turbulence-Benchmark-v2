def palindromes_of_specific_lengths(s):
    s = s[23:78].lower()
    palindromes = set()
    for length in range(13, 41):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes