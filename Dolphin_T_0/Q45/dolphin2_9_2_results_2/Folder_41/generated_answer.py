def palindromes_between_indices(s):
    s = s[2:4]
    palindromes = set()
    for i in range(3, len(s) + 1):
        for j in range(0, len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                palindromes.add(s[j:j + i])
    return palindromes