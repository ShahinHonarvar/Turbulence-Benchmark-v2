def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 91):
        substr = s[i:i + 92]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes