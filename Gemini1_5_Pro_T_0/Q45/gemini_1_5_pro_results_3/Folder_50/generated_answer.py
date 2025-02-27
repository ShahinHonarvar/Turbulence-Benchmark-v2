from collections import Counter

def palindromes_between_indices(string):
    string = string[4:9].lower()
    letters = [letter for letter in string if letter.isalpha()]
    letters_count = Counter(letters)
    palindromes = set()
    if len(letters) >= 5:
        for letter in letters_count:
            if letters_count[letter] >= 2:
                remaining_letters = letters_count.copy()
                remaining_letters[letter] -= 2
                palindromes.update(create_palindromes(letter, remaining_letters))
    return palindromes

def create_palindromes(palindrome, remaining_letters):
    if sum(remaining_letters.values()) == 0:
        return {palindrome + palindrome[::-1]}
    found_palindromes = set()
    for letter in remaining_letters:
        if remaining_letters[letter] >= 2:
            new_palindrome = palindrome + letter
            new_remaining_letters = remaining_letters.copy()
            new_remaining_letters[letter] -= 2
            found_palindromes.update(create_palindromes(new_palindrome, new_remaining_letters))
    if sum(remaining_letters.values()) >= 1:
        for letter in remaining_letters:
            if remaining_letters[letter] == 1:
                new_palindrome = palindrome + letter
                new_remaining_letters = remaining_letters.copy()
                new_remaining_letters[letter] -= 1
                found_palindromes.update(create_palindromes(new_palindrome, new_remaining_letters))
    return found_palindromes