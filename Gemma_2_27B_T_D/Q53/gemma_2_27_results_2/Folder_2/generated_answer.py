def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 54):
        for j in range(i + 54, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(s[i:j])
    return palindromes