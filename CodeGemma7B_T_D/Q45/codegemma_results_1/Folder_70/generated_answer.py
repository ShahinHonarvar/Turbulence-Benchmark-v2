def palindromes_between_indices(text):
    letters = set(text.lower())
    if not letters.issuperset('abcdefghijklmnopqrst'):
        return set()
    palindromes = set()
    for i in range(1, 7):
        for j in range(i + 1, 7):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                if set(substring).issubset(letters):
                    palindromes.add(substring)
    return palindromes