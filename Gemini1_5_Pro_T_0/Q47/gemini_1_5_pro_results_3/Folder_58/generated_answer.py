def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(125, 284):
        for j in range(i + 108, min(284, i + 127)):
            substring = s[i:j]
            if len(substring) >= 109 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes