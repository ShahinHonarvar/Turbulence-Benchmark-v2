def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 22):
        for j in range(i + 23):
            substring = s[i:j + 23]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes