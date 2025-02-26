def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    n = len(letters)
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and is_palindrome(current):
            palindromes.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes