def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = len(s)
    for length in range(30, n + 1):
        for i in range(n - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub)
    return palindromes