from itertools import permutations

def palindromes_between_indices(text):
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 3, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1]:
                unique_letters = set(substring)
                if unique_letters.issubset(set('abcdefghijklmnopqrstuvwxyz')):
                    if not any((elem.isdigit() for elem in unique_letters)):
                        palindromes.add(substring)
    return palindromes