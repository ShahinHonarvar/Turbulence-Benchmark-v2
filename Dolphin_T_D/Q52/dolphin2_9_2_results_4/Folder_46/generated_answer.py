def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    length = 464
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes