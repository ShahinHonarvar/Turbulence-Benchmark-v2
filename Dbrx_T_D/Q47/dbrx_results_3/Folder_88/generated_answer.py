def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11, 88):
        for length in [4, 5]:
            if i + length - 1 < len(s):
                substring = s[i:i + length]
                if substring == substring.lower() and substring.lower() == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes