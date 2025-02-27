def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 24):
        for j in range(i + 13, len(s) - i):
            if s[i:j] == s[i:j][::-1].lower() and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes