def palindromes_of_specific_lengths(s):
    palindromes = set()
    English_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(200, 301):
        for j in range(i, i + 50):
            if j <= len(s):
                palindrome = s[i:j + 1].lower()
                if palindrome and all((letter in English_letters for letter in palindrome)):
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes