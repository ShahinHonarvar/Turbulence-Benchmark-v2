def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(30, 85):
        for j in range(12, 21):
            if i + j - 1 <= 84:
                substring = s[i:i + j].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes