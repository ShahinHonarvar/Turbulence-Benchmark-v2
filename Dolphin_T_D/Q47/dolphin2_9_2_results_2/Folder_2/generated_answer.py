def palindromes_of_specific_lengths(s):
    s = s[10:60]
    palindromes = set()
    for i in range(18, 37):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes