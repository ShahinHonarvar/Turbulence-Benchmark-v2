def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(1, 10):
        for j in range(i, i + 5):
            if s[i - 1:j] == s[i - 1:j][::-1]:
                palindromes.add(s[i - 1:j])
    return palindromes