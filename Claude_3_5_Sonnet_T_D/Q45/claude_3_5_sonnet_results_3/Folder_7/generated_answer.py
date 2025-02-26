def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:10] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for char in set(chars):
            rest = chars.replace(char, '', 1)
            for subpal in generate_palindromes(rest, length - 2):
                result.add(char + subpal + char)
        return result
    palindromes = set()
    for length in range(7, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return set(filter(is_palindrome, palindromes))