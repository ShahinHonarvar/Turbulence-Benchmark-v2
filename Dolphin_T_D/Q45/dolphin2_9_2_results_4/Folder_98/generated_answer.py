def palindromes_between_indices(s):
    s = s[3:6].lower()
    if len(s) >= 4:
        palindromes = set()
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1):
                if s[i:j] == s[j - 1::-1]:
                    palindromes.add(s[i:j])
        return palindromes
    return set()