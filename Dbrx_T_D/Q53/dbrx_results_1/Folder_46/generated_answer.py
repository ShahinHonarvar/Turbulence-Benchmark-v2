def palindrome_of_length_at_least_n(s: str) -> set:
    palindromes = set()
    n = 86
    s = s.lower()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes