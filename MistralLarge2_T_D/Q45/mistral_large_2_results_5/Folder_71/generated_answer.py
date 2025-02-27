def palindromes_between_indices(s):
    letters = [c for c in s[1:4] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and is_palindrome(current):
            palindromes.add(current)
        if not remaining:
            return
        for i in range(len(remaining)):
            new_current = current + remaining[i]
            generate_palindromes(new_current, remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes