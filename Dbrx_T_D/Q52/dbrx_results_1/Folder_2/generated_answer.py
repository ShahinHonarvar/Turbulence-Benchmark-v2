def palindrome_of_length_n(string, n=147):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if set(substring) <= english_letters and all((substring[0] == substring[j] for j in range(n - 1, -1, -2))):
            palindromes.add(substring)
    return palindromes