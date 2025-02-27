def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 75):
        for j in range(76, len(s) - i + 1):
            if s[i:i + j] == s[i:i + j][::-1] and s[i:i + j].isalpha():
                palindromes.add(s[i:i + j])
    return palindromes