def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:8] if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(prefix, remaining, length):
        if length == 0 and is_palindrome(prefix):
            palindromes.add(prefix)
        elif length > 0:
            for i, letter in enumerate(remaining):
                generate_palindromes(prefix + letter, remaining[:i] + remaining[i + 1:], length - 1)
    for length in range(6, len(letters) + 1):
        generate_palindromes('', letters, length)
    return palindromes