def palindromes_between_indices(s):
    substring = s[2:5]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current='', start=0):
        if len(current) >= 3 and is_palindrome(current):
            palindromes.add(current)
        for i in range(start, len(letters)):
            generate_palindromes(letters, current + letters[i], i)
    generate_palindromes(letters)
    return palindromes