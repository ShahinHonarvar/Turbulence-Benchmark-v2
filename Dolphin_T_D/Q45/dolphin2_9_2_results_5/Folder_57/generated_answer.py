def palindromes_between_indices(s):
    s = s[2:6]
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(s) < 5:
        return set()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            if s[i] == s[j - 1]:
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) >= 5:
                    palindromes.add(s[i:j])
    return palindromes