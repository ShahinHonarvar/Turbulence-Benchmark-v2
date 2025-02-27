def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 288):
        if s[i:i + 289] == s[i:i + 289][::-1]:
            palindromes.add(s[i:i + 289])
    return palindromes