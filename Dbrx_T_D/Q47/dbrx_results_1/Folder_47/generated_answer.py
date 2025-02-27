def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(14, 53):
        for start_index in range(39, 95 - length + 1):
            palindrome = s[start_index:start_index + length]
            if all((char in english_letters for char in palindrome)) and palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes