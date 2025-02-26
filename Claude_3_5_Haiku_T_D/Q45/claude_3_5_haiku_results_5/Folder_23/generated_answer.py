def palindromes_between_indices(s):
    s = s.lower()
    letters_in_range = [c for c in s[:7] if c.isalpha()]

    def can_form_palindrome(letters):
        letter_counts = {}
        for letter in letters:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        odd_count = sum((1 for count in letter_counts.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(letters):

        def backtrack(current_letters, used_letters):
            if len(current_letters) == len(letters):
                if can_form_palindrome(current_letters):
                    palindrome_set.add(generate_palindrome(current_letters))
                return
            for i, letter in enumerate(letters):
                if i not in used_letters:
                    current_letters.append(letter)
                    used_letters.add(i)
                    backtrack(current_letters, used_letters)
                    current_letters.pop()
                    used_letters.remove(i)

        def generate_palindrome(arrangement):
            letter_counts = {}
            for letter in arrangement:
                letter_counts[letter] = letter_counts.get(letter, 0) + 1
            center = ''
            sides = []
            for letter, count in letter_counts.items():
                if count % 2 != 0:
                    center = letter
                sides.extend([letter] * (count // 2))
            palindrome = ''.join(sides + [center] + sides[::-1])
            return palindrome
        palindrome_set = set()
        letters = [letter for letter in letters_in_range]
        backtrack([], set())
        return {p for p in palindrome_set if len(p) >= 4}
    return generate_palindromes(letters_in_range)