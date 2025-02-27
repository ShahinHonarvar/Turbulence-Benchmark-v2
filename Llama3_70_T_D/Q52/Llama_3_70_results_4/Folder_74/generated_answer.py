def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 95):
        substr = s[i:i + 96]
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes