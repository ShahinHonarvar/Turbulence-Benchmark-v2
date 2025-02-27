def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 2):
        if s[i:i + 3].isalpha() and s[i:i + 3] == s[i:i + 3][::-1]:
            palindromes.add(s[i:i + 3])
    return palindromes