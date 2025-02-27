from collections import Counter

def palindromes_between_indices(string):
    letters = set((string[i].lower() for i in range(3) if string[i].isalpha()))
    letters_count = Counter((l.lower() for l in string if l.isalpha()))
    palindromes = set()
    for letter in letters:
        if letters_count[letter] >= 2:
            for other_letter in letters:
                if other_letter != letter:
                    word = letter + other_letter * letters_count[other_letter] + letter
                    if len(word) >= 3:
                        palindromes.add(word)
                elif letters_count[letter] >= 3:
                    word = letter * 3
                    if len(word) >= 3:
                        palindromes.add(word)
    return palindromes