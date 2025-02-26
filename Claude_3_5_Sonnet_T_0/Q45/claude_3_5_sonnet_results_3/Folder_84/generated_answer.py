def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, current='', palindromes=set()):
        if len(current) >= 3 and is_palindrome(current):
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char, palindromes)
        return palindromes
    return generate_palindromes(letters)