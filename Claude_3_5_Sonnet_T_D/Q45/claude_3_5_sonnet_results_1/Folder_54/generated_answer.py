def palindromes_between_indices(s):
    letters = ''.join((char.lower() for char in s[4:10] if char.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            rest = chars[:i] + chars[i + 1:]
            for p in generate_palindromes(rest, length - 2):
                result.add(c + p + c)
        return result
    palindromes = set()
    for length in range(4, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return set((p for p in palindromes if is_palindrome(p) and len(p) >= 4))