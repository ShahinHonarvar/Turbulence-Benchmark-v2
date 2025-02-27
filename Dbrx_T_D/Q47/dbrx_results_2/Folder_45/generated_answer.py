def palindromes_of_specific_lengths(s):
    s = s[70:141].lower()
    palindromes = set()
    for i in range(3, 61):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                palindromes.add(s[j:j + i])
    return palindromes