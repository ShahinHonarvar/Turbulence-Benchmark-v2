def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(24, 85):
        for j in range(21, 32):
            if i + j - 1 <= 84:
                substring = s[i:i + j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes