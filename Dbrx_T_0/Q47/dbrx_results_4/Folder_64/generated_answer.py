def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(0, min(8, len(s))):
        for j in range(4, 6):
            if i + j <= len(s):
                substring = s[i:i + j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes