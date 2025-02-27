def palindrome_of_length_n(string):
    string = string.lower()
    pal_length = 16
    palindromes = set()
    for i in range(len(string) - pal_length + 1):
        sub = string[i:i + pal_length]
        if sub == sub[::-1] and sub.isalpha():
            palindromes.add(sub)
    return palindromes