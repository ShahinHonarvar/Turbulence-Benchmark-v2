def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(88, len(s) + 1):
        for start in range(len(s) - length + 1):
            end = start + length
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes