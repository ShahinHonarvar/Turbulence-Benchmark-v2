def palindromes_between_indices(s):
    letters = [c for c in s[2:5] if c.isalpha()]
    lower_letters = [c.lower() for c in letters]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(word):
        if len(word) >= 3 and is_palindrome(word):
            palindromes.add(word)
        if len(word) < len(lower_letters):
            for letter in lower_letters:
                generate_palindromes(word + letter)
    generate_palindromes('')
    return palindromes