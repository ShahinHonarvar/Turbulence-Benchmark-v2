def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[26:88].lower()
    for i in range(52, 57):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                palindromes.add(s[j:j + i])
    return palindromes