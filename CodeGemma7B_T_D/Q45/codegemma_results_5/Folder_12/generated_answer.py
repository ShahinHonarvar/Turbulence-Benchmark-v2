def palindromes_between_indices(s):
    palindromes = set()
    s = s.lower()
    if len(s) < 8:
        return set()
    for i in range(3, 9):
        if len(s) - i < 4:
            break
        for j in range(i + 1, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes