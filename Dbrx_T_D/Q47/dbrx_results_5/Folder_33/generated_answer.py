def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(103, 159):
        for start in range(130, 296 - length + 1):
            palindrome = s[start:start + length]
            if set(palindrome) <= english_letters and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes