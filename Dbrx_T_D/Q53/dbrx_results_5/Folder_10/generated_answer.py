def palindrome_of_length_at_least_n(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s) - 91):
        substring = s[i:i + 92]
        if set(substring) <= english_letters:
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes