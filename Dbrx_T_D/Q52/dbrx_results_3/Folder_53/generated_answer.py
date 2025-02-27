def palindrome_of_length_n(string, n=68):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring[0] not in english_letters:
            continue
        if substring == substring[::-1] and len(set(substring)) <= 26:
            palindromes.add(substring)
    return palindromes