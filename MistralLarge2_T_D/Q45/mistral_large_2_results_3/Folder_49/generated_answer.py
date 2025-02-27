def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[5:8] if ch.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, start, end):
        if len(current) >= 3 and is_palindrome(current):
            palindromes.add(current)
        for i in range(start, end):
            generate_palindromes(current + letters[i], i, end)
    generate_palindromes('', 0, len(letters))
    return palindromes