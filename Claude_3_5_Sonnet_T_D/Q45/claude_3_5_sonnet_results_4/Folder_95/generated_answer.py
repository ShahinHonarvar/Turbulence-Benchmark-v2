def palindromes_between_indices(s):
    letters = ''.join((char.lower() for char in s[7:9] if char.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 2:
            return set()
        if length == 3:
            return {c + m + c for c in chars for m in chars}
        palindromes = set()
        for c in chars:
            for p in generate_palindromes(chars, length - 2):
                palindromes.add(c + p + c)
        return palindromes
    result = set()
    for length in range(3, len(letters) * 2 + 1):
        result.update(generate_palindromes(letters, length))
    return result