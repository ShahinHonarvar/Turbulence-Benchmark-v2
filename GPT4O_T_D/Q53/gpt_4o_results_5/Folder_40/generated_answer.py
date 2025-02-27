def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 2, n):
            substr = s[i:j + 1]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes