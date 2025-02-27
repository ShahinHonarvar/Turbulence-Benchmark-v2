def palindrome_of_length_at_least_n(s: str) -> set:
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 96):
        for j in range(i, len(s)):
            if s[j] == s[i] and j - i + 1 >= 97:
                palindromes.add(s[i:j + 1])
    return palindromes