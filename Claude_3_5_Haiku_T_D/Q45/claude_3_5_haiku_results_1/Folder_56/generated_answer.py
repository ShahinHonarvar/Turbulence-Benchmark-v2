def palindromes_between_indices(s):
    letters = ''.join((char.lower() for char in s[5:10] if char.isalpha()))
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 5 and len(current) == len(remaining) * 2:
            palindromes.add(current)
            return
        for i in range(len(remaining)):
            new_remaining = remaining[:i] + remaining[i + 1:]
            generate_palindromes(remaining[i] + current + remaining[i], new_remaining)

    def recursive_palindrome_generation(letters):
        for length in range(5, len(letters) * 2 + 1, 2):
            generate_palindromes('', sorted(letters))
    recursive_palindrome_generation(letters)
    return palindromes