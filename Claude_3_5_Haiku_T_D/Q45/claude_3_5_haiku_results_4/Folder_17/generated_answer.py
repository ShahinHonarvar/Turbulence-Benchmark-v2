from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    letters = [char for char in substring if char.isalpha()]

    def can_form_palindrome(letter_counts):
        odd_count = sum((1 for count in letter_counts.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(letter_counts):
        palindromes = set()

        def backtrack(current, remaining_chars):
            if not remaining_chars:
                if len(current) >= 4:
                    palindromes.add(current)
                return
            for char in set(remaining_chars):
                new_remaining = list(remaining_chars)
                new_remaining.remove(char)
                backtrack(char + current + char, new_remaining)
        backtrack('', letters)
        return palindromes
    letter_counts = Counter(letters)
    return generate_palindromes(letter_counts) if can_form_palindrome(letter_counts) else set()