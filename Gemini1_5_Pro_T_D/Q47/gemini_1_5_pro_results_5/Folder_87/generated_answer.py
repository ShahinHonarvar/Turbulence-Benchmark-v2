def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11, 94):
        for j in range(i + 33, min(94, i + 54)):
            substring = s[i:j]
            if len(substring) >= 34 and len(substring) <= 54 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes