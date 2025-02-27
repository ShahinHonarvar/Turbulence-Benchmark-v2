def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 85):
        for j in range(i + 43, len(s) - i):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes