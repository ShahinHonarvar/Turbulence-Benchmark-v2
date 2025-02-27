def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(1, 9):
        for length in range(3, 5):
            if i + length <= 9:
                substring = ''.join(filter(str.isalpha, s[i:i + length]))
                if len(substring) == length and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes