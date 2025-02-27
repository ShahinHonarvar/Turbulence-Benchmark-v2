def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 401 + 1):
        substr = s[i:i + 401]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes