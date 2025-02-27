def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 77):
        substr = s[i:i + 78]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes