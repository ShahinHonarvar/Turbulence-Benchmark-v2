def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 76):
        for j in range(10, 21):
            if i + j - 1 <= 75:
                substring = s[i:i + j].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes