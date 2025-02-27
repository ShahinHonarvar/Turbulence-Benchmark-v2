def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    lower_letters = ''.join(letters).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current=''):
        if len(current) >= 5 and is_palindrome(current):
            palindromes.add(current)
        for i in range(len(letters)):
            generate_palindromes(letters[:i] + letters[i + 1:], current + letters[i])
    generate_palindromes(lower_letters)
    return palindromes