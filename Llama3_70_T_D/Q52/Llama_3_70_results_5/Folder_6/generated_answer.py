def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 473):
        substr = s[i:i + 474]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes