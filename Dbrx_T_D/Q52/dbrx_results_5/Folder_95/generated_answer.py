def palindrome_of_length_n(s):
    n = 87
    if len(s) < n:
        return set()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n].lower()
        if substring == substring[::-1] and set(substring) <= set('abcdefghijklmnopqrstuvwxyz'):
            palindromes.add(substring)
    return palindromes