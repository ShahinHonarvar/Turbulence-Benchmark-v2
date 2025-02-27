def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 278):
        if s[i:i + 279] == s[i:i + 279][::-1]:
            palindromes.add(s[i:i + 279])
    return palindromes