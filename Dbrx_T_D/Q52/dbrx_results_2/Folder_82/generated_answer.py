def palindrome_of_length_n(string, n=28):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    if n % 2 == 1:
        mid = n // 2
        for i in range(len(string) - n + 1):
            substring = string[i:i + n]
            if substring[mid] in english_letters and substring[:mid] == substring[mid::-1]:
                palindromes.add(substring)
    else:
        for i in range(len(string) - n + 1):
            substring = string[i:i + n]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes