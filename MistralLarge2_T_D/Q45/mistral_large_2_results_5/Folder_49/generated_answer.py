def palindromes_between_indices(s):
    letters = ''.join((c for c in s[5:8] if c.isalpha())).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, current='', length=3):
        if length == 0:
            if is_palindrome(current):
                palindromes.add(current)
            return
        for char in chars:
            generate_palindromes(chars, current + char, length - 1)
    for length in range(3, len(letters) + 1):
        generate_palindromes(letters, length=length)
    return palindromes