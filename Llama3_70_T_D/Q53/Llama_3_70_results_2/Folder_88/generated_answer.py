def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 27, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes