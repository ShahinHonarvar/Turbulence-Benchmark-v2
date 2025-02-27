def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 90):
        if s[i:i + 91] == s[i:i + 91][::-1] and set(s[i:i + 91]).issubset('abcdefghijklmnopqrstuvwxyz'):
            palindromes.add(s[i:i + 91])
    return palindromes