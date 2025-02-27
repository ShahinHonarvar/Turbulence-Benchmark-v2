def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(17, 73):
        for j in range(i, i + 2):
            if j + 50 > 72:
                break
            substring = s[i:j + 50].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes