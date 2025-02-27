def palindromes_between_indices(s: str) -> set:
    english_letters = set()
    for i in range(ord('a'), ord('z') + 1):
        english_letters.add(chr(i))
    palindromes = set()
    for i in range(1, 9):
        for j in range(i, 9):
            substring = s[i - 1:j].lower()
            if set(substring).difference(english_letters) == set():
                if len(substring) >= 4 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes