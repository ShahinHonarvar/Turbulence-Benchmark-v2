def palindromes_between_indices(s):
    letters = [c for c in s[1:3] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current='', length=3):
        if len(current) == length:
            if is_palindrome(current):
                palindromes.add(current)
            return
        for letter in letters:
            generate_palindromes(letters, current + letter, length)
    for length in range(3, len(letters) + 1):
        generate_palindromes(letters, length=length)
    return palindromes