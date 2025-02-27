def palindromes_between_indices(s):
    chars = [c for c in s[6:9] if c.isalpha()]
    chars = ''.join(chars).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and is_palindrome(current):
            palindromes.add(current)
        if remaining:
            for i in range(len(remaining)):
                generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:])
    generate_palindromes('', chars)
    return palindromes