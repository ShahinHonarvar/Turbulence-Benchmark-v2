def palindromes_of_specific_lengths(s):
    s = s[:7].lower()
    set_of_palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(3, 7):
            if i + j <= n:
                substring = s[i:i + j]
                if substring.isalpha() and substring == substring[::-1]:
                    set_of_palindromes.add(substring)
    return set_of_palindromes