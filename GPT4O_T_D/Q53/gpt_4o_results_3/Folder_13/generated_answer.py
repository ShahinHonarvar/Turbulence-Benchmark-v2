def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for start in range(n):
        for end in range(start + 51, n):
            substring = s[start:end + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes