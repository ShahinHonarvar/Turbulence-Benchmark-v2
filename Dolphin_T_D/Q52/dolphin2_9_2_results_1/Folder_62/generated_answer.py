def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 187):
        if s[i:i + 188] == s[i:i + 188][::-1]:
            palindromes.add(s[i:i + 188])
    return palindromes