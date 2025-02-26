def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[3:10] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 0:
            return ['']
        result = []
        for i in range(len(chars)):
            for p in generate_palindromes(chars[:i] + chars[i + 1:], length - 2):
                result.append(chars[i] + p + chars[i])
        return result
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for p in generate_palindromes(letters, length):
            if is_palindrome(p):
                palindromes.add(p)
    return palindromes