def palindromes_of_specific_lengths(s):
    eng_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = set()
    for length in range(10, 51):
        for i in range(10, 101 - length + 1):
            palindrome = s[i:i + length]
            if set(palindrome) <= eng_letters and palindrome == palindrome[::-1]:
                result.add(palindrome.lower())
    return result