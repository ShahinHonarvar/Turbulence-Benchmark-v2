def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 20):
        for j in range(i, len(s) - i):
            if len(s[i:j + 1]) < 21:
                continue
            if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha():
                palindromes.add(s[i:j + 1])
    return palindromes