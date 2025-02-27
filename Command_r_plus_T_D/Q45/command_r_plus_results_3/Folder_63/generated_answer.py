def palindromes_between_indices(s: str) -> set:

    def is_english_letter(char):
        return char.lower() in 'abcdefghijklmnopqrstuvwxyz'

    def get_english_letters(s):
        return [char.lower() for char in s if is_english_letter(char)]

    def generate_palindromes(letters, left, right):
        if left >= right:
            return [letters]
        palindromes = []
        for i in range(left, right + 1):
            new_letters = letters[:i] + letters[i + 1:]
            palindromes_left = generate_palindromes(new_letters, left, i - 1)
            palindromes_right = generate_palindromes(new_letters, i, right)
            palindromes.extend(palindromes_left)
            palindromes.extend(palindromes_right)
        return palindromes
    english_letters = get_english_letters(s[:4])
    palindromes = generate_palindromes(english_letters, 0, len(english_letters) - 1)
    return {p for p in palindromes if len(p) >= 3}