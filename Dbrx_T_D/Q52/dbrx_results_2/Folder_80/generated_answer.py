def palindrome_of_length_n(string, n=276):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring and set(substring).issubset(english_letters) and (substring == substring[::-1]):
            palindromes.add(substring)
    return palindromes