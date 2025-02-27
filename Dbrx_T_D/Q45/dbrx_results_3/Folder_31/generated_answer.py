def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(1, 9):
        for j in range(i, 9):
            substring = s[i - 1:j]
            if len(substring) >= 6 and set(substring).issubset(english_letters):
                palindrome = substring + substring[-2::-1]
                palindromes.add(palindrome)
    return palindromes