def palindrome_of_length_n(s: str) -> set:
    n = 210
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes