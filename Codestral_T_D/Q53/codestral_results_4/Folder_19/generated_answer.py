def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for l in range(23, len(s) + 1):
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes