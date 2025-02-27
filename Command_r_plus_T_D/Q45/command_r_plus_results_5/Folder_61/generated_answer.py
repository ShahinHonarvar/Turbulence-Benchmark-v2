def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(s[:8])):
        for j in range(i + 7, len(s[:8]) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes