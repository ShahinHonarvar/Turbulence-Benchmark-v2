def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 66):
        for j in range(67):
            if s[i:i + j + 1] == s[i:i + j + 1][::-1] and s[i:i + j + 1].isalpha():
                palindromes.add(s[i:i + j + 1])
    return palindromes