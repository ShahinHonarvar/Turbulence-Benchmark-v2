def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(29, 99):
        for length in range(6, 10):
            if i + length <= 99:
                substring = s[i:i + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes