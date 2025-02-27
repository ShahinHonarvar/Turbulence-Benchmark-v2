def palindrome_of_length_n(string, n=96):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) != n or not all((char in english_letters for char in substring)):
            continue
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes