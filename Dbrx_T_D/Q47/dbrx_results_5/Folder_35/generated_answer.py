def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(34, 91):
        for j in range(14, 40):
            if i + j - 1 <= len(s) and s[i - 1:i + j - 1].lower() == s[i - 1:i + j - 1].lower()[::-1]:
                palindromes.add(s[i - 1:i + j - 1])
    return palindromes