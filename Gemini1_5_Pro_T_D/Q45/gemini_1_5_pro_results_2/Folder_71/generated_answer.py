from collections import Counter

def palindromes_between_indices(string):
    string = string[1:4]
    letters = [letter for letter in string if letter.isalpha()]
    if len(letters) < 4:
        return set()
    letter_counts = Counter(letters)
    palindromes = set()
    for letter in letter_counts:
        palindrome = letter * letter_counts[letter]
        if len(palindrome) >= 4:
            palindromes.add(palindrome.lower())
    return palindromes