def palindrome_of_length_n(string, n=416):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n].lower()
        if set(substring) <= english_letters and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes