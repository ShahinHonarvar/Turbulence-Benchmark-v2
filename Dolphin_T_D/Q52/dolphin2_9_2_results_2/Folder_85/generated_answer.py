def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = 46
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes