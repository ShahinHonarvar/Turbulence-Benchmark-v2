def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for l in range(97, len(s) + 1):
        for i in range(len(s) - l + 1):
            substring = s[i:i + l]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes