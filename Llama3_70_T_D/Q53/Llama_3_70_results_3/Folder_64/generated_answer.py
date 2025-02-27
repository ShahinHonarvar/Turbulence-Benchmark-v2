def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j + 1]
            if substr == substr[::-1] and substr.isalpha() and (len(substr) >= 9):
                palindromes.add(substr)
    return palindromes