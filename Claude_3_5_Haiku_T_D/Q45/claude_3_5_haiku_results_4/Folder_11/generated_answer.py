def palindromes_between_indices(s):
    substring = s[3:8].lower()
    letter_counts = {}
    for char in substring:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    palindromes = set()

    def generate_palindromes(current_letters):
        if len(current_letters) >= 4 and len(current_letters) % 2 == 0:
            half_length = len(current_letters) // 2
            left_half = current_letters[:half_length]
            right_half = current_letters[half_length:]
            if left_half == right_half[::-1]:
                palindromes.add(current_letters)

    def backtrack(remaining_letters, current_letters):
        generate_palindromes(current_letters)
        for letter, count in remaining_letters.items():
            if count > 0:
                new_remaining = remaining_letters.copy()
                new_remaining[letter] -= 1
                if new_remaining[letter] == 0:
                    del new_remaining[letter]
                backtrack(new_remaining, current_letters + letter + letter)
    backtrack(letter_counts, '')
    return palindromes