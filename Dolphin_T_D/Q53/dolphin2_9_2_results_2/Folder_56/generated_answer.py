def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(84, len(s) + 1):
        for j in range(0, len(s) - i + 1):
            substr = s[j:j + i]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes