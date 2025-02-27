def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = s[119:257]
    palindromes = set()
    for i in range(len(s)):
        for j in range(104, 124):
            if i + j <= len(s):
                palindrome = s[i:i + j]
                if palindrome and palindrome == palindrome[::-1] and all((c in english_letters for c in palindrome)):
                    palindromes.add(palindrome)
    return palindromes