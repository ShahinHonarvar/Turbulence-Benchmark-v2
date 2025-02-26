def palindromes_between_indices(s):
    letters = ''.join((char.lower() for char in s[4:10] if char.isalpha()))

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            remaining = chars[:i] + chars[i + 1:]
            for sub_palindrome in generate_palindromes(remaining, length - 2):
                result.add(c + sub_palindrome + c)
        return result
    palindromes = set()
    for length in range(6, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes