from collections import Counter

def palindromes_between_indices(text):
    text = text[3:10]
    letters = [letter.lower() for letter in text if letter.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    if len(letters) >= 3:

        def is_palindrome(word):
            return word == word[::-1]

        def permute(current_word, remaining_letters):
            if not remaining_letters:
                if len(current_word) >= 3 and is_palindrome(current_word):
                    palindromes.add(current_word)
                return
            for letter in remaining_letters:
                updated_letters = remaining_letters.copy()
                updated_letters[letter] -= 1
                if updated_letters[letter] == 0:
                    del updated_letters[letter]
                permute(current_word + letter, updated_letters)
        permute('', letter_counts.copy())
    return palindromes