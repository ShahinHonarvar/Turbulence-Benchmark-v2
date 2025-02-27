def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 13):
        for j in range(i + 7, len(s) - i + 1):
            if len(s[i:j + 1]) >= 14 and s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes