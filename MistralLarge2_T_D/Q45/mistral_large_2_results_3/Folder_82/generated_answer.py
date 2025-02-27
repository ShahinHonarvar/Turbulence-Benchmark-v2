def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:7] if char.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current='', length=7):
        if len(current) == length:
            if is_palindrome(current):
                palindromes.add(current)
            return
        for letter in letters:
            generate_palindromes(letters, current + letter, length)
    generate_palindromes(letters)
    return palindromes