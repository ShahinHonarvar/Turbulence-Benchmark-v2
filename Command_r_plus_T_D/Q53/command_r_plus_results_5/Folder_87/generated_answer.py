def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 17):
        substr = s[i:i + 18]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes