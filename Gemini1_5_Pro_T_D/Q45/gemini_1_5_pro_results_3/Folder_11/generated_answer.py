from collections import Counter

def palindromes_between_indices(string):
    string = string[3:8].lower()
    letters = [letter for letter in string if letter.isalpha()]
    if len(letters) < 4:
        return set()
    letter_counts = Counter(letters)
    palindromes = set()
    for letter in letter_counts:
        if letter_counts[letter] >= 2:
            remaining_letters = list((letter_counts - Counter(letter * 2)).elements())
            if len(remaining_letters) == 0:
                palindromes.add(letter * 2)
            for i in range(len(remaining_letters)):
                for j in range(i + 1, len(remaining_letters)):
                    palindromes.add(letter + remaining_letters[i] + remaining_letters[j] + letter)
    for letter1 in letter_counts:
        if letter_counts[letter1] >= 2:
            for letter2 in letter_counts:
                if letter2 != letter1 and letter_counts[letter2] >= 2:
                    palindromes.add(letter1 * 2 + letter2 * 2)
                    palindromes.add(letter1 + letter2 + letter2 + letter1)
    return palindromes