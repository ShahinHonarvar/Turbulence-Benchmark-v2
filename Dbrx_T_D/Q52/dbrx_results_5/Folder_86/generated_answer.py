def palindrome_of_length_n(string, n=181):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if all((char in english_letters for char in substring)):
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes