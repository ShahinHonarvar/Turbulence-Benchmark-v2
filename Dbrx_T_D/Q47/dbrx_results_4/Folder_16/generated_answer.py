def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(15, 87):
        for j in range(i + 1, 61):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes