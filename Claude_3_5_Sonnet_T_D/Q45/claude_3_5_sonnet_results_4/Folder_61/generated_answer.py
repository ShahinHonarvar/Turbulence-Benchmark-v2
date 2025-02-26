def palindromes_between_indices(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters = [c.lower() for c in s[:8] if c.lower() in alphabet]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for char in chars:
            for palindrome in generate_palindromes(chars, length - 2):
                result.add(char + palindrome + char)
        return result
    palindromes = set()
    for length in range(7, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return set(filter(is_palindrome, palindromes))