def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 25, len(s) + 1):
            substring = ''.join(filter(str.isalpha, s[i:j]))
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes