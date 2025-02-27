def palindrome_of_length_n(string, n=210):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == n and substring == substring[::-1] and (set(substring) <= english_letters):
            palindromes.add(substring)
    return palindromes