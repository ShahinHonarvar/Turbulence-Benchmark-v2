def palindromes_between_indices(s):
    s = s[5:10].lower()
    palindromes = set()
    for i in range(4, len(s) + 1):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                palindromes.add(s[j:j + i])
    return palindromes