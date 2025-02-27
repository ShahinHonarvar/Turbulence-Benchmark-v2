def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 463):
        if s[i:i + 464] == s[i:i + 464][::-1]:
            palindromes.add(s[i:i + 464])
    return palindromes