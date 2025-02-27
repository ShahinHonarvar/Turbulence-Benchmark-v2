def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(1, 6):
        substring = s[0:i].lower()
        if all((char in english_letters for char in substring)):
            if substring == substring[::-1] and len(substring) >= 5:
                palindromes.add(substring)
    return palindromes