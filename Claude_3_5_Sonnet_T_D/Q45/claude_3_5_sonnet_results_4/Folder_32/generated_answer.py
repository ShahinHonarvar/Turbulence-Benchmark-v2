def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:8])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i in range(len(chars)):
            rest = chars[:i] + chars[i + 1:]
            for p in generate_palindromes(rest, length - 2):
                result.add(chars[i] + p + chars[i])
        return result
    palindromes = set()
    for length in range(5, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return set(filter(is_palindrome, palindromes))