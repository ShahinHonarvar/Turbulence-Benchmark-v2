def palindromes_between_indices(input_string):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters = set(input_string[6:9].lower()) & alphabet

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for char in chars:
            for palindrome in generate_palindromes(chars, length - 2):
                result.add(char + palindrome + char)
        return result
    palindromes = set()
    for length in range(4, len(letters) * 2 + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes