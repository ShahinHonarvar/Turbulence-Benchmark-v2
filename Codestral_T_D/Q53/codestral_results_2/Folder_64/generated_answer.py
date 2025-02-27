def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 9
    palindromes = set()
    for length in range(n, len(s) + 1):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes