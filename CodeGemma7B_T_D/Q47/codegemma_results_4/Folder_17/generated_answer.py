def palindromes_of_specific_lengths(s):
    left, right = (22, 95)
    palindromes = set()
    for i in range(left, right + 1):
        for j in range(i, right + 1):
            substring = s[i:j + 1]
            if len(substring) >= 52 and len(substring) <= 55 and (substring == substring[::-1]) and substring.isalpha():
                palindromes.add(substring)
    return palindromes