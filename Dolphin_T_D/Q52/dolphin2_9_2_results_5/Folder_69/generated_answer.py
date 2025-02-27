def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 471):
        if s[i:i + 472] == s[i:i + 472][::-1]:
            palindromes.add(s[i:i + 472])
    return palindromes