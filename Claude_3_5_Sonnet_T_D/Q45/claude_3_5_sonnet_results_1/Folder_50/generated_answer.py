def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 0:
            return ['']
        result = []
        for i in range(len(chars)):
            char = chars[i]
            remaining = chars[:i] + chars[i + 1:]
            for palindrome in generate_palindromes(remaining, length - 2):
                result.append(char + palindrome + char)
        return result
    palindromes = set()
    for length in range(5, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return set(filter(is_palindrome, palindromes))