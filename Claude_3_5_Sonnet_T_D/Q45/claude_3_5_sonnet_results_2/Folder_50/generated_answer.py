def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[4:9] if c.isalpha()))

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for char in set(chars):
            remaining = chars.replace(char, '', 1)
            for sub_palindrome in generate_palindromes(remaining, length - 2):
                result.add(char + sub_palindrome + char)
        return result
    palindromes = set()
    for length in range(5, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes