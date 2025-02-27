def palindrome_of_length_at_least_n(s):
    s = s.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s) - 79):
        substring = s[i:i + 80]
        if all((char in alphabet for char in substring)) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes