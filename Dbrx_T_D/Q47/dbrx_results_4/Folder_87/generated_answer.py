def palindromes_of_specific_lengths(s: str) -> set[str]:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(34, 55):
        for i in range(11, 94 - length + 1):
            palindrome = s[i:i + length]
            if palindrome.lower() == palindrome[::-1].lower() and set(palindrome).issubset(english_letters):
                palindromes.add(palindrome)
    return palindromes