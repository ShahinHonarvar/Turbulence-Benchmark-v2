def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes