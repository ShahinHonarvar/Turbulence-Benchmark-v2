def palindromes_between_indices(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 8):
        for j in range(i, 8):
            substring = string[i:j + 1].lower()
            if len(substring) >= 6 and set(substring) <= english_letters:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes