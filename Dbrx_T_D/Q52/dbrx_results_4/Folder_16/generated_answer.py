def palindrome_of_length_n(string, n=255):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring[:] == substring[::-1] and english_letters.issuperset(substring):
            palindromes.add(substring)
    return palindromes