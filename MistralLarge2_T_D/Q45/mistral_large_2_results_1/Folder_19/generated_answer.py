def palindromes_between_indices(s):
    chars = [c.lower() for c in s[1:8] if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining, length):
        if length >= 7 and is_palindrome(current):
            palindromes.add(current)
        if length >= 7:
            return
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:], length + 1)
    generate_palindromes('', chars, 0)
    return palindromes