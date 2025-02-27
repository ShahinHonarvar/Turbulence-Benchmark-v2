def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set([s[i:i + 27] for i in range(len(s) - 26) if s[i:i + 27] == s[i:i + 27][::-1]])
    return palindromes