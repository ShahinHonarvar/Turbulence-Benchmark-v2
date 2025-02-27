def palindrome_of_length_n(s):
    letters = set('abcdefghijklmnopqrstuvwxyz')
    n = 60
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n].lower()
        if set(substring) <= letters and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes