def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 66):
        if s[i:i + 67] == s[i:i + 67][::-1]:
            palindromes.add(s[i:i + 67])
    return palindromes