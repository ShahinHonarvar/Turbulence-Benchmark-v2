def palindrome_of_length_n(s):
    n = 116
    letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == ''.join(reversed(s[i:i + n])) and all((c in letters for c in s[i:i + n])):
            palindromes.add(s[i:i + n].lower())
    return palindromes