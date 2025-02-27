def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(12, 57):
        for j in range(20, 23):
            if i + j - 1 <= 56 and all((c in english_letters for c in s[i:i + j])):
                palindrome = s[i:i + j]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome.lower())
    return palindromes