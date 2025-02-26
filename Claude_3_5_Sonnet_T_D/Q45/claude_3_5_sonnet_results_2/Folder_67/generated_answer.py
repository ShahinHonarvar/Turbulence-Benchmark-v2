def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:7] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 0:
            return ['']
        result = []
        for i in range(len(chars)):
            for palindrome in generate_palindromes(chars[:i] + chars[i + 1:], length - 2):
                result.append(chars[i] + palindrome + chars[i])
        return result
    palindromes = set()
    for length in range(5, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return set(filter(is_palindrome, palindromes))