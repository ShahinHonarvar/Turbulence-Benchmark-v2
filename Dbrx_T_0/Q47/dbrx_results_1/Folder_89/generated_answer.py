def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(18, 89):
        for length in range(12, 15):
            if i + length <= 88:
                substring = s[i:i + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes