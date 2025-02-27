def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(1, 7):
        substring = s[0:i].lower()
        letters_in_substring = set(substring)
        if letters_in_substring.issubset(english_letters):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes