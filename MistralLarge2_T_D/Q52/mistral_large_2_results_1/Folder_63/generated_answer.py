def palindrome_of_length_n(s):
    n = 18
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - n + 1):
        substr = s_lower[i:i + n]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(s[i:i + n])
    return palindromes