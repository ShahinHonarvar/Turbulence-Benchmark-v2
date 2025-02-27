def palindromes_of_specific_lengths(s):
    palindromes_set = set()
    for i in range(31, 75):
        for j in range(i + 22, min(i + 40, 75) + 1):
            substring = s[i:j]
            if substring == substring.lower() and substring == substring[::-1].lower():
                palindromes_set.add(substring)
    return palindromes_set