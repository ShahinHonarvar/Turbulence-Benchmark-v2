def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(0, len(s) - 45):
        for j in range(i + 45, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes