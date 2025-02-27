def palindrome_of_length_at_least_n(s: str) -> set[str]:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 30):
        for j in range(i + 15, len(s) - i):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes