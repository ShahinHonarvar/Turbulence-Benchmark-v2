def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[j - 1:i:-1] and 3 <= j - i <= 4:
                palindromes.add(s[i:j])
    return palindromes