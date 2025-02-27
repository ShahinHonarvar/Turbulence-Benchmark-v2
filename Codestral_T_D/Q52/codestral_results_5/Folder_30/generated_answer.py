def palindrome_of_length_n(s):
    s = s.lower()
    length = 94
    palindromes = set()
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes