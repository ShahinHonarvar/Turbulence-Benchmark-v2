def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10):
        for length in range(3, 6):
            for j in range(i, i + length + 1):
                substring = s[i:j]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring.lower())
    return palindromes