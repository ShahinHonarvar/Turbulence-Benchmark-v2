def palindrome_of_length_at_least_n(n, string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if english_letters.issuperset(substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes