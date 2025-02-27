def palindrome_of_length_n(string, n=28):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring[0] not in english_letters:
            continue
        if all((char in english_letters for char in substring)) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes