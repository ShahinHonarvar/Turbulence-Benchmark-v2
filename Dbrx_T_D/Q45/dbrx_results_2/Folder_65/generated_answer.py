from collections import defaultdict

def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    english_indices = {index: letter for index, letter in enumerate(s.lower()) if letter in english_letters}
    for i in range(len(english_indices) - 4):
        for j in range(i + 1, min(i + 5, len(english_indices))):
            substring = ''.join((english_indices[index] for index in range(i, j + 1)))
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes