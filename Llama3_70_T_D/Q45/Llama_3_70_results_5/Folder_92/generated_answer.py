def palindromes_between_indices(s):
    s = s[4:8].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes