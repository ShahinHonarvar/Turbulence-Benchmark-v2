def palindromes_of_specific_lengths(s):
    s = s[65:100].lower()
    palindromes = set()
    for i in range(26, 34):
        for j in range(len(s) - i + 1):
            if s[j:i + j] == s[j:i + j][::-1]:
                palindromes.add(s[j:i + j])
    return palindromes