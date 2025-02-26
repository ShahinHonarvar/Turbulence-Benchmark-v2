def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:8])).lower()

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 4

    def generate_palindromes(chars, current=''):
        if len(current) >= 4 and is_palindrome(current):
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char)
            generate_palindromes(chars[:i] + chars[i + 1:], char + current)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes