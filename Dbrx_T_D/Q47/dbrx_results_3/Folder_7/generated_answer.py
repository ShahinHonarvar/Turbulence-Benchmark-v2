def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(119, 256 - 123 + 1):
        for j in range(104, 123 + 1):
            if i + j - 1 <= 256:
                substring = s[i:i + j].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes