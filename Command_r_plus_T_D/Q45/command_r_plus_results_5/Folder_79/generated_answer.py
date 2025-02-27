def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(1, 8):
        for j in range(i + 1, 8):
            substring = s[i:j].lower()
            if all((char in english_letters for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes