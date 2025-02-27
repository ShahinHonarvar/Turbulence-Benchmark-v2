def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(45, 53):
        for i in range(11, 97 - length + 1):
            if s[i:i + length].lower().count('-') == 0 and english_letters.issuperset(s[i:i + length].lower()):
                palindrome = s[i:i + length]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes