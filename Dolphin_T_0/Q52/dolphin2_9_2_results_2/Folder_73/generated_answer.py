def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        if i + 41 <= len(s) + 1:
            substr = s[i:i + 41]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes