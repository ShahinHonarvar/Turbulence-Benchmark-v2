def palindromes_between_indices(s):
    letters = ''.join((ch.lower() for ch in s[2:9] if ch.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            for p in generate_palindromes(chars[:i] + chars[i + 1:], length - 2):
                palindrome = c + p + c
                if len(palindrome) >= 6:
                    result.add(palindrome)
        return result
    palindromes = set()
    for length in range(6, len(letters) + 1):
        palindromes.update(generate_palindromes(letters, length))
    return palindromes