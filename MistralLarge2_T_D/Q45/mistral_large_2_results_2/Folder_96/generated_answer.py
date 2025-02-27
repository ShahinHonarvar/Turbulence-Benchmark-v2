def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 6 and is_palindrome(current):
            palindromes.add(current)
        if remaining:
            for i in range(len(remaining)):
                generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', letters)
    return palindromes