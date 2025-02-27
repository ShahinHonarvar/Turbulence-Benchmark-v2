def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 34, len(s)):
            substring = s[i:j + 1]
            if len(set(substring)) == 1:
                continue
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes