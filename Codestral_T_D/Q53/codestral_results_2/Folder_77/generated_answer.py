def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 149, len(s) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes