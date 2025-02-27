def palindrome_of_length_n(string, n=17):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) != n or not all((char in english_letters for char in substring)) or (not substring.isalpha()):
            continue
        if substring == substring[::-1]:
            palindromes.add(substring.lower())
    return palindromes