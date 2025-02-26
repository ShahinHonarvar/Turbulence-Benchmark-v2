def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[7:10])).lower()

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 3

    def generate_palindromes(chars, current=''):
        if len(current) >= 3 and is_palindrome(current):
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], current + char)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes