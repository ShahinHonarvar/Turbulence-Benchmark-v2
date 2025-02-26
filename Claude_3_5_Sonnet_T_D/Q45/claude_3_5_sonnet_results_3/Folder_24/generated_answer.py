def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, current='', min_length=4):
        if len(current) >= min_length and is_palindrome(current):
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char, min_length)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes