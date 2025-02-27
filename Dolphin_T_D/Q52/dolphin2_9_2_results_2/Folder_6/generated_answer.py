def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 473):
        if s[i:i + 474] == s[i:i + 474][::-1]:
            palindromes.add(s[i:i + 474])
    return palindromes