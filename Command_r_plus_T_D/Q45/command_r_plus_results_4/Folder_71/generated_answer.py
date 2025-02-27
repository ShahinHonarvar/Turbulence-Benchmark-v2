def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(1, min(4, len(s)) + 1):
        substring = s[0:i]
        english_chars = {char for char in substring if char in english_letters}
        if len(english_chars) > 1:
            palindrome = ''.join(sorted(english_chars)) + ''.join(reversed(sorted(english_chars)))
            palindromes.add(palindrome)
    return palindromes