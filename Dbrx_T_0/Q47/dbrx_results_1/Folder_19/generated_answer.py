def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 56):
        for j in range(3, 8):
            if i + j - 1 <= 55:
                substring = s[i:i + j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes