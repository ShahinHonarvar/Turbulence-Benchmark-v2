def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 138
    for i in range(len(s) - n + 1):
        for j in range(i, i + n):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower() and s[i:j + 1].isalpha():
                palindromes.add(s[i:j + 1])
    return palindromes