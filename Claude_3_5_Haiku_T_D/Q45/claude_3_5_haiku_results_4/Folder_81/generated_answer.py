def palindromes_between_indices(s):
    s = s.lower()
    letters = [char for char in s[:7] if char.isalpha()]

    def can_form_palindrome(letter_counts):
        odd_count = sum((1 for count in letter_counts.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(letter_counts):
        palindromes = set()

        def backtrack(current, letter_counts):
            if len(current) >= 3 and can_form_palindrome(letter_counts):
                if len(current) % 2 == 0:
                    palindrome = current + current[::-1]
                else:
                    center_letter = next((letter for letter, count in letter_counts.items() if count % 2 != 0))
                    palindrome = current + center_letter + current[::-1]
                palindromes.add(palindrome)
            for letter, count in list(letter_counts.items()):
                if count > 0:
                    letter_counts[letter] -= 2
                    backtrack(current + letter, letter_counts)
                    letter_counts[letter] += 2
        letter_counts = {letter: letters.count(letter) for letter in set(letters)}
        backtrack('', letter_counts)
        return palindromes
    return generate_palindromes(letter_counts)