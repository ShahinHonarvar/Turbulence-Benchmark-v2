def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 75):
        for length in range(6, 9):
            if i + length <= 75:
                substring = s[i:i + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes