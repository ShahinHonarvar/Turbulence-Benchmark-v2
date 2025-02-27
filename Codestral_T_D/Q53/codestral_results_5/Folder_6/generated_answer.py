def palindrome_of_length_at_least_n(s):
    n = 22
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes