def palindrome_of_length_n(string, n=318):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    string = ''.join((i for i in string if i in english_letters))
    palindromes = {string[i:j] for i in range(len(string)) for j in range(i, min(len(string), i + n) + 1) if string[i:j] == string[i:j][::-1]}
    return palindromes