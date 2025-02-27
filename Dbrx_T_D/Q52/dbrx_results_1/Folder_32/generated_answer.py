def palindrome_of_length_n(string, n=113):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(english_letters & set(substring)) == len(substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes