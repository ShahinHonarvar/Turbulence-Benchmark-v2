def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 92):
        substr = s[i:i + 93]
        for j in range(len(substr)):
            if substr[j] != substr[-j - 1]:
                break
            if j == len(substr) - 1:
                palindromes.add(substr)
    return palindromes