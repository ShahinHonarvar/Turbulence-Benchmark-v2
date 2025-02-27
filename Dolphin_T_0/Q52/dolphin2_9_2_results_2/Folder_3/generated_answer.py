def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substr = s[i:j]
            if len(substr) == 100 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes