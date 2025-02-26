def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for start in range(2, 7):
        for length in range(3, 5):
            if start + length > len(s):
                break
            substring = s[start:start + length]
            if all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes