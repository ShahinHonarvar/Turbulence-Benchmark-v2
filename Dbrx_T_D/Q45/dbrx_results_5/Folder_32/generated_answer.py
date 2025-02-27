def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for start in range(1, min(8, len(s) - 4)):
        for end in range(start, min(8, len(s)) + 1):
            substring = s[start - 1:end]
            if set(substring).issubset(english_letters):
                palindrome = ''.join(sorted(substring, reverse=True))
                if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes