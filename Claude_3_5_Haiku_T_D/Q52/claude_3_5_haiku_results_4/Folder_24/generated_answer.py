def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 28):
        substr = s[i:i + 29]
        if len(substr) == 29 and substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes