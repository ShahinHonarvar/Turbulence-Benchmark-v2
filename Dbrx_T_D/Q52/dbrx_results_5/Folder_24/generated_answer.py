def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 29 + 1):
        if s[i:i + 29] == s[i:i + 29][::-1]:
            palindromes.add(s[i:i + 29])
    return palindromes