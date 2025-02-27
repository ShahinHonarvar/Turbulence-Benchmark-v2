from collections import Counter

def palindromes_between_indices(string):
    letters = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    relevant_letters = []
    for i in range(3):
        if string[i].lower() in letters:
            relevant_letters.append(string[i].lower())
    if len(relevant_letters) == 0:
        return set()
    letter_counts = Counter(relevant_letters)
    palindromes = set()
    for letter in letter_counts:
        if letter_counts[letter] >= 3:
            palindromes.add(letter * 3)
        for other_letter in letter_counts:
            if letter != other_letter and letter_counts[letter] >= 2 and (letter_counts[other_letter] >= 1):
                palindromes.add(letter * 2 + other_letter)
                palindromes.add(letter + other_letter + letter)
    return palindromes