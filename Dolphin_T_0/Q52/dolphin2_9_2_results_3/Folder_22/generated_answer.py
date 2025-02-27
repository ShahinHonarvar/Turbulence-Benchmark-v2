def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 19):
        if s[i:i + 20] == s[i:i + 20][::-1]:
            palindromes.add(s[i:i + 20])
    return palindromes