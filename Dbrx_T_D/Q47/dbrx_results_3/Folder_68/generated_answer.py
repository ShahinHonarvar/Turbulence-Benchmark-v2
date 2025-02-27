def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(50, 101):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes