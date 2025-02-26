def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:9])).lower()
    if len(letters) < 4:
        return set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i in range(len(chars)):
            for palindrome in generate_palindromes(chars[:i] + chars[i + 1:], length - 2):
                result.add(chars[i] + palindrome + chars[i])
        return result
    palindromes = set()
    for length in range(4, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return set(filter(is_palindrome, palindromes))