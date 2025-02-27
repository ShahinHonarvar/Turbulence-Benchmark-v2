def palindrome_of_length_n(string, n=18):
    letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n].lower()
        if substring.isalpha() and all((letter in letters for letter in substring)) and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes