def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:5] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 0:
            yield ''
        elif len(chars) == 0:
            return
        else:
            for i, c in enumerate(chars):
                for p in generate_palindromes(chars[:i] + chars[i + 1:], length - 2):
                    yield (c + p + c)
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in generate_palindromes(letters, length):
            if is_palindrome(p):
                palindromes.add(p)
    return palindromes