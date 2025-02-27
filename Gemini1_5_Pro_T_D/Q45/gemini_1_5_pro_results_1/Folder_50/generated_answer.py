from collections import Counter

def palindromes_between_indices(string):
    string = string[4:9].lower()
    letters = [letter for letter in string if letter.isalpha()]
    if len(letters) < 5:
        return set()
    letter_counts = Counter(letters)
    palindromes = set()
    for letter1 in letter_counts:
        for letter2 in letter_counts:
            if letter1 == letter2:
                if letter_counts[letter1] >= 5:
                    palindromes.add(letter1 * 5)
                if letter_counts[letter1] >= 3:
                    palindromes.add(letter1 * 3)
            else:
                if letter_counts[letter1] >= 2 and letter_counts[letter2] >= 2:
                    palindromes.add(letter1 * 2 + letter2 * letter_counts[letter2] + letter1 * 2)
                if letter_counts[letter1] >= 2 and letter_counts[letter2] >= 1:
                    palindromes.add(letter1 * 2 + letter2 + letter1 * 2)
    return palindromes