def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(32, 72):
        for j in range(21, 33):
            if i + j - 1 <= 71:
                substring = s[i:i + j].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes