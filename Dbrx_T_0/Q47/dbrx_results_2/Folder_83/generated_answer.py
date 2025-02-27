def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(75, 96):
        for length in range(7, 10):
            if i + length <= 95:
                substring = s[i:i + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes