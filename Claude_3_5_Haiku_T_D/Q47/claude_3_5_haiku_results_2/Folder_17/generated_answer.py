def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[22:96].lower()
    for length in range(52, 56):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes