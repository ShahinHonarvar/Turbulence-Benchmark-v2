def palindrome_of_length_at_least_n(s: str) -> set:
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 98):
        for j in range(99):
            if s[i + j] != s[i + j + 99]:
                break
            palindrome = s[i:i + j + 100]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes