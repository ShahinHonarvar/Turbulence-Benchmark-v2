from collections import Counter

def palindromes_between_indices(text):
    text = text[4:10].lower()
    letters = [letter for letter in text if letter.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    if len(letters) >= 5:

        def is_palindrome(word):
            return len(word) >= 5 and word == word[::-1]

        def backtrack(current_word, remaining_letters):
            if not remaining_letters:
                if is_palindrome(current_word):
                    palindromes.add(current_word)
                return
            for letter in list(remaining_letters):
                remaining_letters[letter] -= 1
                if remaining_letters[letter] == 0:
                    del remaining_letters[letter]
                backtrack(current_word + letter, remaining_letters.copy())
        backtrack('', letter_counts.copy())
    return palindromes