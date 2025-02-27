def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(36, len(s) + 1):
        for j in range(i - 1, len(s) + 1):
            sub = s[j - i:j]
            if sub == sub.lower():
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes