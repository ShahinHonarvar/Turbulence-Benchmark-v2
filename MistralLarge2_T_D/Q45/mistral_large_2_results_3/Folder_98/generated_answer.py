def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6] if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current='', start=0):
        if len(current) >= 4 and is_palindrome(current):
            palindromes.add(current)
        for i in range(start, len(letters)):
            generate_palindromes(letters, current + letters[i], i)
    generate_palindromes(letters)
    return palindromes