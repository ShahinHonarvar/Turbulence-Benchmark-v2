def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    english_letters.update('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(3, 9):
        substring = s[3:i]
        substring_set = set(substring.lower())
        if substring_set.issubset(english_letters):
            if substring == substring[::-1] and len(substring) >= 5:
                palindromes.add(substring)
    return palindromes