def palindrome_of_length_n(string, n=42):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    if len(string) < n:
        return palindromes
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if set(substring) <= english_letters and substring == substring[::-1]:
            palindromes.add(substring.lower())
    return palindromes