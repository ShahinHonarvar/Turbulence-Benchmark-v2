def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 76):
        for j in range(i - 20, i - 9):
            if j >= 0 and j < len(s):
                substring = s[j:i].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes