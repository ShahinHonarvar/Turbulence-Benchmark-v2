def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 2):
        if s[i].isalpha() and s[i + 2].isalpha() and (s[i] == s[i + 2]):
            palindromes.add(s[i:i + 3])
    return palindromes