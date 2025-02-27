def palindromes_of_specific_lengths(s):
    s = s[29:97].lower()
    palindromes = set()
    for i in range(12, 19):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                palindromes.add(s[j:j + i])
    return palindromes