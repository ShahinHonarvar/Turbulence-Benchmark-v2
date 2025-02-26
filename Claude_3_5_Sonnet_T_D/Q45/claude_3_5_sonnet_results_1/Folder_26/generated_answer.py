def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:7])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        if len(chars) <= 1:
            return set(chars)
        result = set()
        for i, c in enumerate(chars):
            for p in generate_palindromes(chars[:i] + chars[i + 1:]):
                new_pal = c + p + c
                if len(new_pal) >= 3 and is_palindrome(new_pal):
                    result.add(new_pal)
        return result
    return generate_palindromes(letters)