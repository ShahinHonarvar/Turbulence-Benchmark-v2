def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(43, 48):
        for j in range(16, 78 - i + 1):
            if s[j:j + i].lower() == s[j:j + i][::-1].lower():
                palindromes.add(s[j:j + i])
    return palindromes