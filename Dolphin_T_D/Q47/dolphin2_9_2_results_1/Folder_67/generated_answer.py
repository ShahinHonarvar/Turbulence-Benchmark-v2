def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(65, 100):
        for j in range(i, 100):
            substring = s[i:j + 1]
            if 26 <= len(substring) <= 33 and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes