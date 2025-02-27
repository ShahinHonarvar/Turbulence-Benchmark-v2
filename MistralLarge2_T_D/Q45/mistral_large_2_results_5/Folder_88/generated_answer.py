def palindromes_between_indices(s):
    substring = s[3:8].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining, length):
        if length >= 6 and is_palindrome(current):
            palindromes.add(current)
        if not remaining:
            return
        for i in range(len(remaining)):
            generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:], length + 1)
    generate_palindromes('', letters, 0)
    return palindromes