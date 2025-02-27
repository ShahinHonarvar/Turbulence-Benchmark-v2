def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(75, 96):
        for j in range(7, 10):
            if i + j - 1 <= i:
                break
            if s[i:i + j] == s[i:i + j][::-1]:
                palindromes.add(s[i:i + j])
    return palindromes