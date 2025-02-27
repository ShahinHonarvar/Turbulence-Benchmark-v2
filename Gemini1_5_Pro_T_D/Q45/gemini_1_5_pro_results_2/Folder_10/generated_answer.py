from collections import Counter

def palindromes_between_indices(string):
    string = string[0:6].lower()
    letters = [letter for letter in string if letter.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    if len(letters) < 3:
        return palindromes

    def form_palindromes(current_palindrome, letter_counts):
        if len(current_palindrome) >= 3:
            palindromes.add(current_palindrome)
        for letter in letter_counts:
            if letter_counts[letter] >= 2:
                letter_counts[letter] -= 2
                form_palindromes(letter + current_palindrome + letter, letter_counts)
                letter_counts[letter] += 2
            if letter_counts[letter] >= 1:
                letter_counts[letter] -= 1
                form_palindromes(letter + current_palindrome + letter, letter_counts)
                letter_counts[letter] += 1
    form_palindromes('', letter_counts)
    return palindromes