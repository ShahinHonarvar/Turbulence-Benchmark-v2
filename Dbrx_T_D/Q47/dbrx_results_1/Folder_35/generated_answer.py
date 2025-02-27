def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(14, 40):
        for i in range(34, 91 - length):
            palindrome = s[i:i + length]
            if set(palindrome) <= english_letters and palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes