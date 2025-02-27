def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[26:85].lower()
    for i in range(len(s) - 29):
        for j in range(30, 47):
            substring = s[i:i + j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes