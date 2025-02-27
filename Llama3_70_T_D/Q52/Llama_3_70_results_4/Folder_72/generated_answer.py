def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 15):
        substr = s[i:i + 16]
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes