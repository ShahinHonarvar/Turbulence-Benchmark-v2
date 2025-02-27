from collections import Counter

def palindromes_between_indices(string):
    string = string[2:7].lower()
    letters = [letter for letter in string if letter.isalpha()]
    letters_count = Counter(letters)
    palindromes = set()
    if len(letters) < 4:
        return palindromes

    def inner(palindrome):
        if len(palindrome) >= 4:
            palindromes.add(palindrome)
        for letter in letters_count:
            if letters_count[letter] >= 2:
                letters_count[letter] -= 2
                inner(letter + palindrome + letter)
                letters_count[letter] += 2
        if len(palindrome) + 1 >= 4:
            palindromes.add(palindrome)
        for letter in letters_count:
            if letters_count[letter] >= 1:
                letters_count[letter] -= 1
                inner(palindrome + letter)
                letters_count[letter] += 1
    inner('')
    return palindromes