def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:6])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        if len(chars) <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            for p in generate_palindromes(chars[:i] + chars[i + 1:]):
                new_p = c + p + c
                if len(new_p) >= 5 and is_palindrome(new_p):
                    result.add(new_p)
        return result
    return generate_palindromes(letters)