def palindromes_of_specific_lengths(s):
    s = s[100:300]
    palindromes = set()
    for i in range(50, 101):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if all((c.isalpha() for c in substring)) and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes