def palindrome_of_length_n(string, n=95):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring[0] not in english_letters:
            continue
        if substring == substring[::-1] and all((letter in english_letters for letter in substring)):
            palindromes.add(substring.lower())
    return palindromes