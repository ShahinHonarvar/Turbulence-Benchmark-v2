def palindrome_of_length_n(string, n=28):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1] and set(substring).issubset(english_letters):
            palindromes.add(substring)
    return palindromes