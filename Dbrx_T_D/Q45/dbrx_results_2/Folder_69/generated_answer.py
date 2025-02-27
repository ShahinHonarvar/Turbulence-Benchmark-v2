def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 4:
        return set()
    palindromes = set()
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(i, j + 1):
                palindrome = s[k]
                if k - 1 >= 0 and s[k - 1] == s[k]:
                    palindrome = s[k - 1] + palindrome
                if j < len(s) - 1 and s[j + 1] == s[j]:
                    palindrome += s[j + 1]
                palindromes.add(palindrome)
    return palindromes