def palindrome_of_length_at_least_n(s):
    s = s.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s) - 86):
        if set(s[i:i + 87]).issubset(alphabet) and s[i:i + 87] == s[i:i + 87][::-1]:
            palindromes.add(s[i:i + 87])
    return palindromes