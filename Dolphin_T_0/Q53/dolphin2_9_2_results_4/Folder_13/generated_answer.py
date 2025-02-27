def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 52
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            if sub.isalpha():
                palindromes.add(sub)
    return palindromes