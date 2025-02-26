def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:8])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for char in chars:
            for palindrome in generate_palindromes(chars.replace(char, '', 1), length - 2):
                result.add(char + palindrome + char)
        return result
    palindromes = set()
    for length in range(6, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes