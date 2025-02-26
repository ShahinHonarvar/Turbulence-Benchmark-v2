def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:9] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 4
    palindromes = set()

    def generate_palindromes(current, remaining):
        if is_palindrome(current):
            palindromes.add(current)
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes