def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(13, 41):
        for i in range(23, 78 - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes