from collections import Counter

def palindromes_between_indices(string):
    letters = Counter([string[i].lower() for i in range(0, 7) if string[i].isalpha()])
    palindromes = set()
    for letter in letters:
        if letters[letter] >= 2:
            for other_letter in letters:
                if letters[other_letter] >= 2 and letter != other_letter:
                    palindromes.add(2 * letter + 2 * other_letter)
                    palindromes.add(2 * other_letter + 2 * letter)
    for letter in letters:
        if letters[letter] >= 4:
            palindromes.add(4 * letter)
    for letter in letters:
        if letters[letter] >= 3:
            for other_letter in letters:
                if other_letter != letter:
                    palindromes.add(3 * letter + other_letter)
                    palindromes.add(other_letter + 3 * letter)
    return palindromes