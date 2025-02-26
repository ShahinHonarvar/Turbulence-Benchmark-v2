def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:4] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 3

    def generate_palindromes(chars, current='', used=None):
        if used is None:
            used = set()
        if is_palindrome(current):
            palindromes.add(current)
        for i, char in enumerate(chars):
            if i not in used:
                generate_palindromes(chars, current + char, used | {i})
    palindromes = set()
    generate_palindromes(letters)
    return palindromes