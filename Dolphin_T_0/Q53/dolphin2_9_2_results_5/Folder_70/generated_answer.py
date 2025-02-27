def palindrome_of_length_at_least_n(s):
    s = s.replace('_', '').lower()
    palindromes = set()
    for i in range(11, len(s) + 1):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes