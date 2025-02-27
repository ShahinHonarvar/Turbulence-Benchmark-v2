def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(17, 96):
        for length in range(13, 50):
            if i + length - 1 <= 95:
                substring = s[i:i + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes