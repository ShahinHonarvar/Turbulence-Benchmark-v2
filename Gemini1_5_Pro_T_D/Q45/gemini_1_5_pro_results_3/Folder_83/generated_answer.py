from collections import Counter

def palindromes_between_indices(string):
    string = string[2:10].lower()
    letters = [letter for letter in string if letter.isalpha()]
    if len(letters) < 7:
        return set()
    letter_counts = Counter(letters)
    palindromes = set()
    for letter in letter_counts:
        palindrome = letter * letter_counts[letter]
        if len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes