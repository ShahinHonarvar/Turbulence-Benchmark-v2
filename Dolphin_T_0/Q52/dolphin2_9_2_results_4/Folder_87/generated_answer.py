def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 56):
        if s[i:i + 57] == s[i:i + 57][::-1]:
            palindromes.add(s[i:i + 57])
    return palindromes