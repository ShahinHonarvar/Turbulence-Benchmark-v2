def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:4] if c.isalpha()]
    if len(letters) < 2:
        return set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, current='', length=0):
        if length >= 4:
            if is_palindrome(current):
                palindromes.add(current)
        for i in range(len(chars)):
            generate_palindromes(chars[:i] + chars[i + 1:], current + chars[i], length + 1)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes