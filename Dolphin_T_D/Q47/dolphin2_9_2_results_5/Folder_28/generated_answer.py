def palindromes_of_specific_lengths(s):
    s = s[32:72]
    palindromes = set()
    for length in range(21, 33):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                if all((char.isalpha() for char in substring)):
                    palindromes.add(substring.lower())
    return palindromes