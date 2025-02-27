def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 136):
        substr = s[i:i + 137]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes