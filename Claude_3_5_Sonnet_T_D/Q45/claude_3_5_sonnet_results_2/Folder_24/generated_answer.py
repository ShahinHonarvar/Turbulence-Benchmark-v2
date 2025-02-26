def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:10] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            remaining = chars[:i] + chars[i + 1:]
            for inner in generate_palindromes(remaining, length - 2):
                result.add(c + inner + c)
        return result
    palindromes = set()
    for length in range(4, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return set((p for p in palindromes if len(p) >= 4 and is_palindrome(p)))